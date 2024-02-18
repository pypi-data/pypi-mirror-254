# %%
import sys
import time
import os
import argparse
import numpy as np

sys.path.append("./")
from varaps.util import mode1
from varaps.util import mode2


def get_input_with_default(prompt, default):
    user_input = input(prompt + f" (default: {default}): ")
    return user_input.strip() if user_input.strip() != "" else default


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


def get_files(fpath, mode):
    """
    get all bam files in a directory if given, if it is a file, return the file name.
    """
    files_to_analyse = []
    isFile = os.path.isfile(fpath)

    # checks if path is a directory
    isDirectory = os.path.isdir(fpath)

    if mode == 1 or mode == 3:
        file_extension = (".bam", ".cram")
        prefix = ""
    elif mode == 2:
        file_extension = ".csv"
        prefix = "Xsparse_"

    files_to_analyse = []
    if isFile and fpath.endswith(file_extension):
        files_to_analyse.append(fpath)
    elif isDirectory:
        for file in os.listdir(fpath):
            if file.startswith(prefix) and file.endswith(file_extension):
                files_to_analyse.append(os.path.join(fpath, file))
    else:
        print("The path is invalid.")

    if len(files_to_analyse) == 0:
        print("No files to analyse")
        return None

    files_to_analyse.sort()
    print("Files to analyse: ", *files_to_analyse, sep="\n")
    return files_to_analyse


def main():
    # get files to analyse from command line
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument(
        "-m",
        "--mode",
        help="Mode selection (Choose 1, 2 or 3): \n 1 - Retrieve mutations from each read found in BAM/CRAM files. \n 2 - Get variants proportions from mode 1 output. \n 3 - Get variants proportions directly from BAM/CRAM files.\n",
        type=int,
        choices=[1, 2, 3],
    )
    parser.add_argument(
        "--path",
        help="path to the directory containing bam/cram files or to the bam/cram file directly",
    )
    parser.add_argument("--ref", help="path to the reference sequence file")
    parser.add_argument(
        "-o",
        "--output",
        help="path to the output directory (default: current directory)",
    )
    parser.add_argument(
        "-p",
        "--filter_per",
        help="percentage of reads that must contain a mutation to be kept as a mutation (default: 0.0)",
        type=float,
    )
    parser.add_argument(
        "-n",
        "--filter_num",
        help="number of reads that must contain a mutation to be kept as a mutation (default: 0)",
        type=int,
    )

    parser.add_argument(
        "--deconv_method",
        help="deconvolution method: \n 1 - Co-occurence based methode\n 2 - Count based method\n 3 - Frequencies based method\n(only applicable in Mode 2 and Mode 3) (default: 1):",
        type=int,
        # choices=[1, 2, 3, 4],
    )
    # parser.add_argument for Matrix M (profile mutation variant matrix)
    parser.add_argument(
        "--M",
        help="Path to the profile mutation variant matrix (only applicable in Mode 2 and Mode 3)",
    )
    # parser.add_argument for number of Bootstraps
    parser.add_argument(
        "--NbBootstraps",
        help="Number of bootstraps (only applicable in Mode 2 and Mode 3), default: 1",
        type=int,
    )
    # parser.add_argument for True/False optimize by Error Rate (alpha) also
    parser.add_argument(
        "--optibyAlpha",
        help="Optimise by alpha - True/False optimize by Error Rate (alpha) also - (only applicable in Mode 2 and Mode 3), default: True",
    )
    # parser.add_argument for alphaInit
    parser.add_argument(
        "--alphaInit",
        help="Initial value for Error Rate alpha (only applicable in Mode 2 and Mode 3), default: 0.01",
        type=float,
    )

    # parse the arguments
    args = parser.parse_args()

    # input questions
    # Check if required arguments are missing and prompt for input if necessary
    if args.mode is None:
        inp = input(
            "Mode selection (Choose 1, 2 or 3): \n 1 - Retrieve mutations from each read found in BAM/CRAM files. \n 2 - Get variants proportions from mode 1 output. \n 3 - Get variants proportions directly from BAM/CRAM files.\n Mode selection (Choose 1, 2 or 3): "
        )
        if inp:
            args.mode = int(inp)
        else:
            args.mode = 1

    if args.mode == 1 or args.mode == 3:
        while args.path is None or not (os.path.isfile(args.path) or os.path.isdir(args.path)):
            args.path = input("Enter path to bam/cram file or directory: ")

        if args.ref is None:
            while args.ref is None or not os.path.isfile(args.ref):
                args.ref = input("Enter path to the reference sequence file: ")

        if args.output is None or not os.path.isdir(args.output):
            args.output = input("Enter path to result folder (defaut current folder): ")
        if args.filter_per is None or args.filter_per not in range(0, 101):
            args.filter_per = input("Enter percentage of reads that must contain a mutation to be kept as a mutation (defaut 0.0): ")
            if args.filter_per:
                args.filter_per = float(args.filter_per)

        if args.filter_num is None or args.filter_num == "" or args.filter_num < 0:
            args.filter_num = input("Enter number of reads that must contain a mutation to be kept as a mutation (default 0): ")
            if args.filter_num:
                args.filter_num = int(args.filter_num)

    if args.mode == 2 or args.mode == 3:
        if args.deconv_method is None or not args.deconv_method in range(1, 5):
            inp = input("Enter deconvolution method: \n 1 - Co-occurence based methode\n 2 - Count based method\n 3 - Frequencies based method\nDeconvolution method(Choose 1,2 or 3)(default 1): ")
            if inp:
                args.deconv_method = int(inp)
            else:
                args.deconv_method = 1

        if (args.path is None or not (os.path.isfile(args.path) or os.path.isdir(args.path))) and args.mode and args.mode == 2:
            args.path = input("Enter path to X files folder/file: ")

        if (args.path is None or not (os.path.isfile(args.path) or os.path.isdir(args.path))) and args.mode == 3:
            args.path = input("Enter path to bam/cram file or directory: ")

        if args.output is None or not os.path.isdir(args.output):
            args.output = input("Enter path to result folder: ")
        if args.M is None or not os.path.isfile(args.M):
            args.M = input("Enter path to profile mutation variant matrix: ")
        if args.NbBootstraps is None or not args.NbBootstraps in range(1, 1000):
            args.NbBootstraps = input("Enter number of bootstraps (default 1): ")
            if args.NbBootstraps:
                args.NbBootstraps = int(args.NbBootstraps)
        if args.optibyAlpha is None or not args.optibyAlpha in [
            True,
            False,
            "True",
            "False",
            "true",
            "false",
            "T",
            "F",
            "t",
            "f",
            "1",
            "0",
            1,
            0,
        ]:
            args.optibyAlpha = input("Enter if optimized also by Error Rate alpha should be (default True): ")
            if args.optibyAlpha:
                args.optibyAlpha = bool(eval(args.optibyAlpha))
        if args.alphaInit is None or args.alphaInit == "":
            args.alphaInit = input("Enter initial value for Error Rate alpha (default 0.01): ")
            if args.alphaInit:
                args.alphaInit = float(args.alphaInit)
    if args.mode == 3:
        if args.path is None or not (os.path.isfile(args.path) or os.path.isdir(args.path)):
            args.path = input("Enter path to bam/cram file or directory: ")

        if args.ref is None or not os.path.isfile(args.ref):
            while args.ref is None or not os.path.isfile(args.ref):
                args.ref = input("Enter path to the reference sequence file: ")

        if args.filter_per is None or args.filter_per == "":
            args.filter_per = input("Enter percentage of reads that must contain a mutation to be kept as a mutation(default 0.0): ")
            if args.filter_per:
                args.filter_per = float(args.filter_per)

        if args.filter_num is None or args.filter_num == "" or args.filter_num < 0:
            args.filter_num = input("Enter number of reads that must contain a mutation to be kept as a mutation (default 0): ")
            if args.filter_num:
                args.filter_num = int(args.filter_num)

    # Set default values for optional arguments
    if args.path is None or not (os.path.isfile(args.path) or os.path.isdir(args.path)):
        if args.mode == 1 or args.mode == 3:
            args.path = input("Enter path to bam/cram file or directory: ")
        elif args.mode == 2:
            args.path = input("Enter path to X files folder/file: ")

    if args.filter_per is None or args.filter_per == "":
        args.filter_per = 0.0

    if args.filter_num is None or args.filter_num == "" or not args.filter_num in range(0, 1001):
        args.filter_num = 0

    if args.output is None or not os.path.isdir(args.output):
        args.output = os.getcwd()

    if args.NbBootstraps is None or args.NbBootstraps == "" or not args.NbBootstraps in range(1, 1000):
        args.NbBootstraps = 1
    if args.optibyAlpha is None or not args.optibyAlpha in [
        True,
        False,
        "True",
        "False",
        "true",
        "false",
        "T",
        "F",
        "t",
        "f",
        "1",
        "0",
        1,
        0,
    ]:
        args.optibyAlpha = True

    if args.alphaInit is None or args.alphaInit == "":
        args.alphaInit = 0.01

    if args.deconv_method is None or args.deconv_method == "" or not args.deconv_method in range(1, 5):
        args.deconv_method = 1

    # Existing code for argument values
    fpath = args.path
    ref_path = args.ref
    output_dir = args.output
    filter_per = args.filter_per
    filter_num = args.filter_num
    print("args.optibyAlpha = ", args.optibyAlpha)
    # check if optibyAlpha is not a boolean
    if not isinstance(args.optibyAlpha, bool):
        optibyAlpha = bool(eval(args.optibyAlpha))
    else:
        optibyAlpha = args.optibyAlpha

    files_to_analyse = get_files(fpath, args.mode)
    if files_to_analyse is None:
        exit()

    global_start_time = time.time()
    if args.mode == 1:
        for file_name in files_to_analyse:
            mode1.analyze_file_mode1(file_name, ref_path, filter_per, filter_num, output_dir)
    if args.mode == 2:
        mode2.analyze_file_mode2(
            fpath,
            args.M,
            output_dir,
            args.NbBootstraps,
            args.alphaInit,
            optibyAlpha,
            args.deconv_method,
        )
    if args.mode == 3:
        rand_id = np.random.randint(0, 10000000)
        temp_output_dir = os.path.join(output_dir, f"temp_X_Matrix_{rand_id}")
        if not os.path.exists(temp_output_dir):
            try:
                os.makedirs(temp_output_dir, exist_ok=True)
            except OSError:
                print("Creation of the directory %s failed" % temp_output_dir)
        for file_name in files_to_analyse:
            mode1.analyze_file_mode1(file_name, ref_path, filter_per, filter_num, temp_output_dir)
        mode2.analyze_file_mode2(
            temp_output_dir,
            args.M,
            output_dir,
            args.NbBootstraps,
            args.alphaInit,
            optibyAlpha,
            args.deconv_method,
        )

    # print("time to save csv file:", time.time() - startTime)
    print("**** total time: ", round(time.time() - global_start_time, 2), "s ****")


if __name__ == "__main__":
    main()
