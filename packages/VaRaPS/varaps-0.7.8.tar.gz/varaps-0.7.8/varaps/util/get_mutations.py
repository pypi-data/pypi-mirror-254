# %%
from cigar import Cigar
from collections import Counter, defaultdict
import time
from tqdm import tqdm
import bisect

# import pandas as pd
import numpy as np
import pandas as pd


def get_mutations(startPos, cigarStr, seq, ref):
    """
    returns a list of mutations detected in the given read.

    INPUTS:
    startPos: positive integer; 0-based starting position in the reference sequence of the read.
    cigarStr: CIGAR string of the read's alignment.
    seq: string; the read sequence.
    ref: string; the refernce to which the read is compared to find mutations (substitutions, deletions and insertions)

    OUTPUTS:
    mutations: a set of strings containing all mutations found. Notation examples:
    A100T: in 1-based indexation, the 100th letter of the reference sequence is A but the given read is substituted by T;
    AC100A: in 1-based indexation, the 100th and the 101st letters of the reference sequence are AC but the given read has a deletion at the 101st position;
    A100AC: in 1-based indexation, the 100th letter of the reference sequence is A but the given read has an insertion at the 101st position, the letter inserted is C;

    an integer indicating the last 0-based position of the reference sequence covered by the given read.
    """

    # to be returned
    mutations = set()

    shift = 0  # lag between the starting point of the read in the REF seq and the real valid starting point
    qryPos = 0  # index that goes through the QUERY seq
    cigars = list(Cigar(cigarStr).items())

    for cigar in cigars:
        # flag situations and update qryPos and/or shift

        ## D := deletion, N := skipped [consumes Q: no; consumes Ref: yes]
        ## => only the shift moves forward, qry index stays put
        if cigar[1] in ["D", "N"]:
            # in case of deletion
            if cigar[1] == "D":
                mutations.add(
                    ref[startPos + shift - 1 : startPos + shift + cigar[0]]
                    + str(startPos + shift)
                    + ref[startPos + shift - 1]
                )
            qryPos += 0
            shift += cigar[0]

        ## H := hard clipping, P := padding [consumes Q: no; consumes Ref: no]
        ## => do nothing and go to the next cigar WITHOUT moving any positions
        elif cigar[1] in ["H", "P"]:
            continue

        ## I := insertion, S:= soft clip [consumes Q: yes; consumes Ref: no]
        ## => only the qry index moves forward, shift stays put
        elif cigar[1] in ["I", "S"]:
            # in case of insertion
            if cigar[1] == "I":
                mutations.add(
                    ref[startPos + shift - 1]
                    + str(startPos + shift)
                    + ref[startPos + shift - 1]
                    + seq[qryPos : qryPos + cigar[0]]
                )
            qryPos += cigar[0]
            shift += 0

        else:
            if cigar[1] in ["M", "X"]:
                mutations = mutations.union(
                    {
                        ref[min(startPos + shift + i, len(ref) - 1)]
                        + str(startPos + shift + i + 1)
                        + seq[min(qryPos + i, len(seq) - 1)]
                        for i in range(cigar[0])
                        if ref[min(startPos + shift + i, len(ref) - 1)]
                        != seq[min(qryPos + i, len(seq) - 1)]
                    }
                )
            qryPos += cigar[0]
            shift += cigar[0]

    return mutations, startPos + shift


def extract_positions(mut_str):
    """
    returns the position (extract digits from a string) in a mutation string
    """
    return int("".join([i for i in mut_str if i.isdigit()]))


def check_if_in_interval(num, interval):
    """
    returns True if position is in the interval, False otherwise
    """
    return num >= interval[0] and num <= interval[1]


def weighted_concatenate(lists, weight):
    """
    returns a numpy array of mutations found in lists repeated weight time (needed to calculate excat number of occurence of each mutation).
    CAREFUL: weight here is not the count of each read but the count of "counts of each read"
    """
    if weight > 1:
        return np.repeat(np.concatenate(lists), weight)
    if len(lists) == 1:
        return np.array(lists[0])
    return np.concatenate(lists)


def coverage_profile(readInfoDF, nbPositions):
    """
    returns a dict with the number of reads covering each position.
    OUTPUT:
    a dict with keys = positions and values = number of reads covering that position
    """
    readInfoDF["Counts_intervals"] = readInfoDF.groupby(
        ["startIdx_0Based", "endIdx_0Based"]
    )["Counts"].transform("sum")
    temp = readInfoDF.drop_duplicates(
        subset=["startIdx_0Based", "endIdx_0Based", "Counts_intervals"]
    )
    coverage = {pos: 0 for pos in range(nbPositions + 1)}
    for _, row in tqdm(
        temp.iterrows(), total=temp.shape[0], desc="Step 3/3 - Creat coverage profile"
    ):
        for pos in range(row["startIdx_0Based"], row["endIdx_0Based"]):
            coverage[pos] += row["Counts_intervals"]
    return coverage


def humansize(nbytes):
    """
    returns a human-readable string representation of a number of bytes.

    INPUTS:
    nbytes: integer; number of bytes
    OUTPUTS:
    a string with the number of bytes in a human-readable format
    """
    suffixes = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.0
        i += 1
    f = ("%.2f" % nbytes).rstrip("0").rstrip(".")
    return "%s %s" % (f, suffixes[i])


def get_all_mutations(readInfoDf, refseq, filter_per=0.01, filter_num=5):
    """
    Get mutations for each read and concatenate them together.

    INPUTS:
    readInfoDf: pandas dataframe; contains information about each read
    refseq: string; reference sequence
    filter_per: float; <Filter par>percentage of reads that must contain a mutation to be kept as a mutation
    filter_num: integer; <Filter par> number of reads that must contain a mutation to be kept as a mutation

    OUTPUTS:
    1. results_relative_mutation_index:a pandas dataframe with the following columns:
        - "startIdx_mutations_Based": integer; first mutaions indice[in mutations_kept] in the read
        - "endIdx_mutations_Based": integer; last mutaions indice[in mutations_kept] in the read
        - "muts": string; mutations found in the read separated by a comma
        - "Counts": integer; number of times the read was found in the bam file
    2. results_ablolute_positions: a pandas dataframe with the following columns:
        - "startIdx_0Based": integer; start position of the read in the reference sequence
        - "endIdx_0Based": integer; end position of the read in the reference sequence
        - "muts": string; mutations found in the read separated by a comma
        - "Counts": integer; number of times the read was found in the bam file

    3. mutations_kept: a list of mutations that were kept after filtering, ordered by position in the reference sequence
    """

    tqdm.pandas(desc="Step 2/3 - get_all_mutations for each read")
    res = readInfoDf.progress_apply(
        lambda x: get_mutations(
            x["startIdx_0Based"], x["CIGAR"], x["Sequence"], refseq
        ),
        axis=1,
        result_type="reduce",
    )
    # print("TOTAL memory usage of res: ", humansize(sys.getsizeof(res)))
    readInfoDf["endIdx_0Based"] = [read[1] for read in res]
    weights = list(readInfoDf["Counts"].values)
    # print("len weights", len(weights))

    startTime = time.time()

    all_count = defaultdict(int)
    for i, set_mut in enumerate(res):
        for mut in set_mut[0]:
            # print("i ", i, "mut ", mut, "weights[i] ", weights[i])
            all_count[mut] += weights[i]
            pass
    # print("time to convert to dict and counts: ", time.time() - startTime)
    # print("memory usage of all_count: ", humansize(sys.getsizeof(all_count)))

    startTime = time.time()

    coverage = coverage_profile(readInfoDf, len(refseq))
    # print("Nb of all mutation detected in the bam file ", len(all_count))
    # print("Filter mutations...")
    keepMuts = {
        var
        for var, cnt in all_count.items()
        if cnt >= max(coverage[extract_positions(var)] * filter_per, filter_num)
    }  # Keep only mutations that accure at least <filter_per>% of the reads that cover that position AND at least in <filter_num> reads
    # print("time to keep mutations:", time.time() - startTime)
    # print("keepMuts.shape", len(keepMuts))
    keepMuts = {
        mutStr for mutStr in keepMuts if not (("N" in mutStr) or ("=" in mutStr))
    }
    startTime = time.time()
    mutation_position_dict = {var: extract_positions(var) for var in keepMuts}
    # print("time to extract positions:", time.time() - startTime)
    startTime = time.time()
    sorted_mutation_position_dict = {
        k: [v]
        for k, v in sorted(mutation_position_dict.items(), key=lambda item: item[1])
    }
    # print("time to sort positions:", time.time() - startTime)
    startTime = time.time()
    mutations_kept = []
    for i, k in enumerate(sorted_mutation_position_dict):
        sorted_mutation_position_dict[k].append(i)
        mutations_kept.append(k)
    startTime = time.time()
    results = pd.DataFrame(
        {
            "startIdx_0Based": readInfoDf["startIdx_0Based"].values,
        }
    )
    results["endIdx_0Based"] = readInfoDf["endIdx_0Based"].values
    results["Counts"] = readInfoDf["Counts"].values

    del readInfoDf  # free memory
    # free readInfoDf memory
    filtred_mut_kept_temp = [set_mut[0].intersection(keepMuts) for set_mut in res]
    # print big variables memory usage
    # get the index of the mutation in the keepMuts array
    startTime = time.time()
    filtred_mut_kept = [
        sorted([sorted_mutation_position_dict[mut][1] for mut in set_mut])
        for set_mut in filtred_mut_kept_temp
    ]
    results["muts"] = filtred_mut_kept
    results["muts"] = results["muts"].apply(tuple)
    # remove duplicates based on start and end mutatios's position in the reference sequence
    startTime = time.time()
    results_ablolute_positions = (
        results.groupby(["startIdx_0Based", "endIdx_0Based", "muts"])
        .agg({"Counts": "sum"})
        .reset_index()
    )
    # print("time to groupby results_ablolute_positions:", time.time() - startTime)

    # Update start and end index to be relative to mutations, not absulute to the reference
    results_relative_mutation_index = results_ablolute_positions.copy()
    all_positions = [v[0] for v in sorted_mutation_position_dict.values()]
    results_relative_mutation_index[
        "startIdx_mutations_Based"
    ] = results_relative_mutation_index["startIdx_0Based"].apply(
        lambda x: min(len(mutations_kept) - 1, bisect.bisect_left(all_positions, x + 1))
    )
    results_relative_mutation_index[
        "endIdx_mutations_Based"
    ] = results_relative_mutation_index["endIdx_0Based"].apply(
        lambda x: bisect.bisect_right(all_positions, x + 1)
    )
    # remove duplicates based on start and end mutatio index
    # print("time to create dataframe:", time.time() - startTime)
    startTime = time.time()
    results_relative_mutation_index = (
        results_relative_mutation_index.groupby(
            ["startIdx_mutations_Based", "endIdx_mutations_Based", "muts"]
        )
        .agg({"Counts": "sum"})
        .reset_index()
    )
    # print("time to groupby:", time.time() - startTime)
    results_relative_mutation_index["muts"] = (
        results_relative_mutation_index["muts"].astype(str).str.strip("(|)")
    )
    results_ablolute_positions["muts"] = (
        results_ablolute_positions["muts"].astype(str).str.strip("(|)")
    )

    # print("size of results dataframe: ", humansize(results.memory_usage(index=True, deep=True).sum()))
    print("Exporting results...")
    return results_relative_mutation_index, results_ablolute_positions, mutations_kept


# %%
