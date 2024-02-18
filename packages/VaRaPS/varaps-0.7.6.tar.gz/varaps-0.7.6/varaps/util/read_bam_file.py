import pysam
import numpy as np
import pandas as pd
import time
from tqdm import tqdm


results = []  # i_order, start, cigar, seq
counts = {}  # (start, seq): count


def read_bam_file(path_to_file):
    """
    convert a bam/cram file into a dataframe

    INPUT:
    path_to_file: string, path to the bam/cram file to be converted.

    OUTPUT:
    a dataframe containing 4 columns:
    0-based start indices, CIGAR strings, sequence strings and the counts of apperance of a read.
    """
    read_mode = "rb" if path_to_file.endswith(".bam") else "rc" if path_to_file.endswith(".cram") else None
    pysam.index(path_to_file)
    bam = pysam.AlignmentFile(path_to_file, read_mode)
    contig, nbReads = np.array(bam.get_index_statistics()[0])[[0, -1]]
    nbReads = int(bam.count())
    print("*number of reads: ", nbReads)
    return read_to_df(bam, contig, nbReads)


def read_read(args):
    """
    read a read from a bam/cram file
    """
    global results
    global counts
    i = args[0]
    elem = args[1]
    start, cigar, seq = np.array(str(elem).split("\t"))[[3, 5, 9]]
    start = int(start) - 1  # make it 0-based
    # to be returned
    if (start, seq) in counts:
        counts[(start, seq)] += 1
    else:
        counts[(start, seq)] = 1
        results.append([i, start, cigar, seq])


def humansize(nbytes):
    """
    Convert a number of bytes to a human-readable string.

    INPUT:
    nbytes: int, number of bytes
    OUTPUT:
    a string containing the number of bytes in a human-readable format.
    """
    suffixes = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.0
        i += 1
    f = ("%.2f" % nbytes).rstrip("0").rstrip(".")
    return "%s %s" % (f, suffixes[i])


def read_to_df(bam, contig, nbReads):
    """
    read a bam/cram file and return a dataframe containing 4 columns:
    0-based start indices, CIGAR strings, sequence strings and the counts of apperance of a read.
    """
    global results
    global counts
    results = []
    counts = {}
    startTime = time.time()
    iterator = bam.fetch(contig)

    for i, elem in enumerate(tqdm(iterator, total=int(nbReads), desc="Step 1/3 - reading bam/cram file")):
        read_read((i, elem))

    results = list(zip(*results))
    # print("*-* time big for bam.fetch(contig): ", time.time() - startTime)
    startTime = time.time()
    readInfoDf = pd.DataFrame.from_dict({"startIdx_0Based": results[1], "CIGAR": results[2], "Sequence": results[3]})
    readInfoDf.startIdx_0Based = readInfoDf.startIdx_0Based.astype(np.int32)
    readInfoDf["Counts"] = readInfoDf.apply(lambda X: counts[(X.startIdx_0Based, X.Sequence)], axis=1)
    readInfoDf = readInfoDf.loc[readInfoDf.CIGAR.apply(lambda x: x[0] in "1234567890")]
    # print("memory usage of readInfoDf's cols:\n", readInfoDf.memory_usage(index=True, deep=True).apply(humansize))
    # print("TOTAL memory usage of readInfoDf: ", humansize(readInfoDf.memory_usage(index=True, deep=True).sum()))
    # print("*-* time for counting reads weights : ", time.time() - startTime)
    return readInfoDf
