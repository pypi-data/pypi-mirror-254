# VaRaPS: Variant Read Proportion System

## Introduction
VaRaPS (Variant Read Proportion System) is a Python package designed for calculating the proportions of each SARS-CoV-2 variant from sequencing data. It supports BAM and CRAM file formats and re-implements methods like Freyja, LCS, and VirPool. VaRaPS is equipped with three modes of operation to cater to various analysis needs.

## Table of Contents
1. [Installation](#installation)
2. [Features](#features)
3. [Quick Start](#quick-start)
4. [Usage](#usage)
   - [Interactive Mode](#interactive-mode)
   - [Mode 1: Retrieve Mutations](#mode-1-retrieve-mutations)
   - [Mode 2: Calculate Variant Proportions](#mode-2-calculate-variant-proportions)
   - [Mode 3: Direct Calculation from Files](#mode-3-direct-calculation-from-files)
5. [Understanding the Output of mode 1](#understanding-the-output)
<!-- 6. [Dependencies](#dependencies) -->
6. [Troubleshooting](#troubleshooting)
7. [Contributors](#contributors)
8. [License](#license)

## Installation
```
pip install VaRaPS
```
Ensure   that   Python   3.8 or later version   is   installed   on   your   system   before   installing   VaRaPS.

## Features

* Implements multiple methods for variant proportion calculations.
* Offers three modes [Co-occurence based methode, Count based method and Frequencies based method] for flexible analysis requirements.
* Interactive mode prompts users through the analysis process.
* Supports both BAM and CRAM file formats.

## Quick Start

For a quick start, you can run VaRaPS in an interactive mode which will guide you through the process:

```shell
varaps
```

Follow the on-screen prompts to input your data and choose the analysis parameters.

## Usage

VaRaPS is designed to be flexible and user-friendly, offering several modes and parameters to fit your analysis needs. Below are detailed explanations of how to use each mode and what each parameter means.

##### General Command Structure

All commands in VaRaPS follow a basic structure:

```bash
varaps --mode <mode_number> [options]
```

Replace `<mode_number>` with the mode you wish to use (1, 2, or 3), and `[options]` with the various options available for that mode, detailed below.

#### Mode 1: Retrieve Mutations

This mode extracts mutations from reads in BAM/CRAM files, by Doing a variant calling for each read(e.g line in the BAM/CRAM file)

```bash
varaps --mode 1 --path <path_to_bam_cram_files> --ref <path_to_reference_fasta> [--output <output_directory>] [--percentage <filter_percentage>] [--number <filter_number>]
```

* `--path <path_to_bam_cram_files>`: Specify the directory containing your BAM/CRAM files.
* `--ref <path_to_reference_fasta>`: Indicate the path to your reference genome file in FASTA format.
* `--output <output_directory>`: (Optional) Designate where you want the results to be saved. By default, results are saved in the current directory.
* `--percentage <filter_percentage>`: (Optional) Set the minimum percentage of reads that must contain a mutation for it to be considered significant. The default is 0.0, which means no filtering is applied based on percentage.
* `--number <filter_number>`: (Optional) Define the minimum number of reads that must contain a mutation for it to be recognized. The default is 0, which means no filtering is applied based on read count.

#### Mode 2: Calculate Variant Proportions

In this mode, VaRaPS calculates the proportion of each variant using the output from Mode 1 or directly from BAM/CRAM files.

```bash
varaps --mode 2 --deconv_method <method_number> --NbBootstraps <number_of_bootstraps> --optibyAlpha <optimize_by_alpha> --alphaInit <initial_alpha_value> --path <path_to_data> [--output <output_directory>] --M <path_to_variant_matrix>
```

* `--deconv_method <method_number>`: Choose the deconvolution method to use. The number corresponds to the specific implementation, where:
   * 1 - Co-occurence based methode
   * 2 - Count based method
   * 3 - Frequencies based method
* `--path <path_to_data>`: Specify the path to the input data, which can be the output directory from Mode 1.
* `--M <path_to_variant_matrix>`: Provide the path to the variant/mutation profile matrix, which is a CSV file with rows representing variants and columns representing mutations.
* `--output <output_directory>`: (Optional) Indicate the output directory for the results.

* `--NbBootstraps <number_of_bootstraps>`: (Optional) Set the number of bootstrap iterations for estimating uncertainty.
* `--optibyAlpha <optimize_by_alpha>`: (Optional) Boolean value (`True` or `False`) to determine if the algorithm should optimize by error rate.
* `--alphaInit <initial_alpha_value>`: (Optional) Provide the initial value for the error rate parameter.

#### Mode 3: Direct Calculation from Files

Mode 3 combines the functionality of Modes 1 and 2 for a direct calculation of variant proportions from BAM/CRAM files without the intermediate step.

```bash
varaps --mode 3 --path <path_to_bam_cram_files> --ref <path_to_reference_fasta> --deconv_method <method_number> [--other_options]
```

* The parameters for Mode 3 are a combination of those from Modes 1 and 2.
* Use the same `--path`, `--ref`, `--output`, and `--deconv_method` parameters as described above.
* Include any other optional parameters as needed to refine your analysis.


## Understanding the Output

VaRaPS generates detailed output files that encapsulate the results of the mutation and variant analysis. Below are the explanations of the files along with examples to help you understand their structure and content.
#### mutations_index File

- **Filename**: `mutations_index_<input_file_name>_<options>.csv`
- **Contents**: Lists all mutations, that passed the filter, found in the input files, serving as an index for the mutations referenced in the Xsparse file.
- **Example**:
```
Mutations
T6TC
C9A
A11G
A11T
AAA14A
A16G
A16AG
...
...
```
 - **Interpretation**:
    - Each line represents a unique mutation, identified by a combination of the reference base, the position in the reference sequence, and the alternate base.
    - This file acts as a legend for the mutation indices used in the Xsparse file[e.i The mutation at index 4 is `AAA14A`.]

#### Mutation Encoding

- **Format**: `[reference base][position][alternate base]`
- **Example**:
- `T6TC` indicates a substitution at position 6 where 'T' has been replaced by 'C'.
- `AAA14A` suggests a deletion at position 14 where 'AAA' has been shortened to 'A'.
- `A16AG` describes an insertion at position 16 where 'G' has been added after 'A'.

#### Xsparse File

- **Filename**: `Xsparse_<input_file_name>_<options>.csv`
- **Contents**: The Xsparse file contains a list of reads and the mutations they contain, represented in a sparse matrix format.The `Xsparse` file is the most important file as it contains the actual data.
- **Example**:
```

startIdx_position,endIdx_position,muts
0,4,
0,44,"0, 2"
0,22,"3,"
1,150,"1, 4"
2,275,"2, 5, 6"
...
...
```

**Interpretation**:
- The columns `startIdx_position` and `endIdx_position` define the range of positions covered by a read.
- The `muts` column lists the indices of the mutations present in the read within the defined range.
- For instance:
    - In read 0, it covers the region from position 0  inclusive to position 4 exclusive. It has no mutations.
    - In read 4, it covers the region from position 2 inclusive to position 75 exclusive. The mutations 2, 5, and 6 are found in this read.

#### Wsparse File

- **Filename**: `Wsparse_<input_file_name>_<options>.csv`
- **Contents**: This file associates each read with its frequency in the dataset to optimize data storage.
- **Example**:
```
Counts
2
1
1
1
5
...
...
```


**Interpretation**:
- Each line corresponds to the reads as they are listed in the Xsparse file.
- The `Counts` column indicates how many times each respective read appears in the dataset [e.i - Read 4 occurs 5 times in the data.]
## Troubleshooting
If you encounter any issues while using VaRaPS, please contact us at djaout [at] lpsm.paris
## Contributing

Contributions to VaRaPS are welcome. If you have suggestions or improvements, feel free to mail me at djaout[at]lpsm.paris

## License

GNU General Public License v3 or later (GPLv3+)
## Contact

For any questions or feedback regarding VaRaPS, feel free to reach out through by mail at djaout[at]lpsm.paris






