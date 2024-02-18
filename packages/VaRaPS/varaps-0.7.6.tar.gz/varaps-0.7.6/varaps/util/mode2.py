# %%
import numpy as np
import time
import pandas as pd
import sys
import os
import bisect

from ast import literal_eval

from concurrent.futures import ProcessPoolExecutor
from functools import partial

sys.path.append("./")
# from VariantsProportionCoOcc import VariantsProportionCoOcc
from varaps.util import VariantsProportionCoOcc
from varaps.util import VariantsProportionFreyjaSparse
from varaps.util import VariantsProportionFreyja1Sparse
from varaps.util import VariantsProportionLCS
import warnings

warnings.filterwarnings("ignore")


# %%
def get_files(fpath):
    # checks if path is a file
    isFile = os.path.isfile(fpath)

    # checks if path is a directory
    isDirectory = os.path.isdir(fpath)

    files_to_analyse = []
    if isFile and fpath.endswith(".csv"):
        files_to_analyse.append(fpath)
    elif isDirectory:
        for file in os.listdir(fpath):
            if file.startswith("Xsparse_") and file.endswith(".csv"):
                files_to_analyse.append(os.path.join(fpath, file))
                # files_to_analyse.append(fpath + "/" + file)
    else:
        print("The path is not a file or a directory")

    if len(files_to_analyse) == 0:
        print("No files to analyse")
        # return
    # print("Files to analyse: ", *files_to_analyse, sep="\n")
    files_to_analyse.sort()

    files_to_analyse = np.array(files_to_analyse)
    # reverse the order of the files
    files_to_analyse = files_to_analyse[::-1]
    return files_to_analyse


# %%
def get_sample_bootstrap_weight(weights):
    positions = np.random.choice(
        np.arange(len(weights)),
        size=np.sum(weights),
        replace=True,
        p=weights / np.sum(weights),
    )
    return np.bincount(positions, minlength=len(weights))


def extract_positions(mut_str):
    """
    returns the position (extract digits from a string) in a mutation string
    """
    return int("".join([i for i in mut_str if i.isdigit()]))


# PATH_X_MATRIXs = "../../EauDeParis/X_sparse"
# PATH_RESULT = "../../EauDeParis/X_sparse_result"
# PATH_M_MATRIX = "../../Arnaud/proposed_lineages_list4SUMMIT.stringent.freyja0001.csv"
# NbBootstraps = 10
# alphaInit = 0.01
# freezeAlpha = False
# files_to_analyze = get_files(PATH_X_MATRIXs)


def analyse_file(file, PATH_RESULT, PATH_M_MATRIX, NbBootstraps, alphaInit, optibyAlpha, decov_method=1):
    M = pd.read_csv(PATH_M_MATRIX, index_col=0)

    variants = M.index.values
    # M = pd.read_csv('data/MmatrixFreyjaOldDelsFULL.csv', index_col=0)
    # M = M.T
    muts_data_df = pd.read_csv(file)
    Weights_df = pd.read_csv(file.replace("Xsparse_", "Wsparse_"))
    mut_idx_df = pd.read_csv(file.replace("Xsparse_", "mutations_index_"))
    muts_data = [set(literal_eval(x)) if not pd.isna(x) else set() for x in muts_data_df.muts.values]

    starts_idx = muts_data_df.startIdx_0Based.values
    ends_idx = muts_data_df.endIdx_0Based.values

    Weights = Weights_df.Counts.values
    muts_idx = mut_idx_df.Mutations.values

    # print('Number of mutations in M matrix: ', M.shape[1])
    # print('Number of mutations in bam: ', len(muts_idx))
    muts_in_bam_and_M = set(muts_idx).intersection(set(M.columns))
    muts_to_analyse = set(M.columns)
    muts_to_analyse = {mut: extract_positions(mut) for idx, mut in enumerate(muts_to_analyse)}
    muts_to_analyse = {k: v for k, v in sorted(muts_to_analyse.items(), key=lambda item: item[1])}
    all_positions = list(muts_to_analyse.values())
    # Update start and end index to be relative to mutations, not absulute to the reference
    starts_idx_new = muts_data_df["startIdx_0Based"].apply(lambda x: min(len(muts_to_analyse) - 1, bisect.bisect_left(all_positions, x + 1)))
    starts_idx_new = starts_idx_new.to_numpy()
    ends_idx_new = muts_data_df["endIdx_0Based"].apply(lambda x: bisect.bisect_right(all_positions, x + 1))
    ends_idx_new = ends_idx_new.to_numpy()
    # update mutations_index to take into account the mutations that are not present in bam but present in M matrix
    temp_muts_dict = {mut: [idx, muts_to_analyse[mut]] for idx, mut in enumerate(muts_to_analyse.keys())}
    muts_idx_new = [temp_muts_dict[mut][0] for mut in muts_in_bam_and_M]
    muts_data_new = []
    for mut_set in muts_data:
        res = set()
        for mut in mut_set:
            if muts_idx[mut] in muts_in_bam_and_M:
                res.add(temp_muts_dict[muts_idx[mut]][0])
        muts_data_new.append(res)
    muts_data_new = np.array(muts_data_new)

    M = M[list(muts_to_analyse.keys())].to_numpy().T
    nM, nV = M.shape
    mutations = np.array(list(muts_to_analyse.keys()))

    resCooc = np.zeros((NbBootstraps, 6 + nV))
    top5_list = []
    print("Number of reads: ", np.sum(Weights))
    # Decov method
    if decov_method == 1:
        decov_func = VariantsProportionCoOcc.VariantsProportionCoOcc
        decov_name = "CoOcc"
    elif decov_method == 2:
        decov_func = VariantsProportionLCS.VariantsProportionLCS
        decov_name = "LCS"
    elif decov_method == 4 or decov_method == 3:
        decov_func = VariantsProportionFreyja1Sparse.VariantsProportionFreyja1Sparse
        decov_name = "Freyja1Sparse"

    for i in range(NbBootstraps):
        print("Bootstrap: ", i + 1)
        weight = get_sample_bootstrap_weight(Weights)  # Do the bootstrap on the weights not on the X matrix to reduce the memory usage
        start = time.time()
        res_decov = decov_func(
            starts_idx_new,
            ends_idx_new,
            muts_data_new,
            M,
            alphaInit=alphaInit,
            readsCount=weight,
        )
        res_decov()
        res_decov.fit(freezeAlpha=not optibyAlpha)
        # if np.abs(pi0 - pi000)<0.001:
        result = res_decov.params
        if decov_method == 3 or decov_method == 4:
            result = res_decov.solution
        # order result idx by decreasing order
        idxs = np.argsort(result)[::-1]

        # save result
        # get top 5 name variants with highest proportion of co-occurrence with their proportion on str

        top5 = [variants[i] + ": " + str(result[i]) + "|" for i in idxs[:5]]
        # convert list to string
        top5 = "".join(top5)
        top5_list.append(top5[:-1])
        resCooc[i, :nV] = result
        resCooc[i, nV] = res_decov.alpha
        resCooc[i, nV + 1] = res_decov.nbIter_alpha_fixed
        resCooc[i, nV + 2] = res_decov.time_alpha_fixed
        resCooc[i, nV + 3] = res_decov.nbIter_alpha
        resCooc[i, nV + 4] = res_decov.time_alpha
        resCooc[i, nV + 5] = res_decov.time_used
        # print(top5)

    # save result df
    resCooc_df = pd.DataFrame(
        resCooc,
        columns=list(variants)
        + [
            "alpha",
            "nbIter_alpha_fixed",
            "time_alpha_fixed",
            "nbIter_alpha",
            "time_alpha",
            "time_used",
        ],
    )
    resCooc_df["top5"] = top5_list
    resCooc_df["file"] = file.replace("Xsparse_", "").split("/")[-1]
    # make file first column and top5 second column
    cols = resCooc_df.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    resCooc_df = resCooc_df[cols]
    resCooc_df["nbReads"] = np.sum(Weights)
    resCooc_df["nbMutations"] = len(mutations)

    # convert to int
    resCooc_df["nbReads"] = resCooc_df["nbReads"].astype(int)
    resCooc_df["nbMutations"] = resCooc_df["nbMutations"].astype(int)
    resCooc_df["nbIter_alpha_fixed"] = resCooc_df["nbIter_alpha_fixed"].astype(int)
    resCooc_df["nbIter_alpha"] = resCooc_df["nbIter_alpha"].astype(int)
    # save result on csv
    # creat result folder if it does not exist
    out_dir = os.path.join(PATH_RESULT, decov_name)
    if not os.path.exists(out_dir):
        abs_path = os.path.abspath(out_dir)
        print("creating directory: ", abs_path)
        os.makedirs(abs_path, exist_ok=True)
    save_path = os.path.join(out_dir, file.replace("Xsparse_", "").split("/")[-1])
    print("saving :", save_path)
    resCooc_df.to_csv(save_path, index=False)


def analyze_file_mode2(path_X, path_M, path_result, nb_bootstrap, alpha_init, optibyAlpha, decov_method=1, max_workers_=3):
    PATH_X_MATRIXs = path_X
    PATH_RESULT = path_result
    PATH_M_MATRIX = path_M
    NbBootstraps = nb_bootstrap
    alphaInit = alpha_init
    optibyAlpha = optibyAlpha
    files_to_analyze = get_files(PATH_X_MATRIXs)
    max_workers = min(max_workers_, len(files_to_analyze))
    # analyse_file(files_to_analyze[0], PATH_RESULT=PATH_RESULT, PATH_M_MATRIX=PATH_M_MATRIX, NbBootstraps=NbBootstraps, alphaInit=alphaInit, optibyAlpha=optibyAlpha, decov_method=decov_method)

    func = partial(analyse_file, PATH_RESULT=PATH_RESULT, PATH_M_MATRIX=PATH_M_MATRIX, NbBootstraps=NbBootstraps, alphaInit=alphaInit, optibyAlpha=optibyAlpha, decov_method=decov_method)
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        executor.map(func, files_to_analyze)
