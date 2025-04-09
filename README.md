# Online Appendix Repository

## Overview

This repository serves as the online appendix for our paper on code-to-code translation using large language models (LLMs). It provides the full experimental framework, including code, data, visualizations, and supplementary analyses to ensure full transparency and reproducibility of our findings. The experiments focus on evaluating translation success and failure across various programming languages by capturing four distinct error types.

## Repository Structure

- **Code**  
  This directory contains the source code used for the experiments. It includes:
  - **RunsJsonData**: A subdirectory that holds JSON files detailing the configuration options for each experiment.
  - **Prompts**: The exact prompts can be found in RunsJsonData for each experiment.

- **Data**  
  This section contains all the experimental results. The data is organized into folders that hold CSV files for four types of errors:
  - **Compilation errors**  
  - **Test errors**  
  - **Runtime errors**  
  - **Infinite Loop errors**  

  Each CSV file represents a matrix where rows correspond to target languages and columns correspond to source languages. Each cell is assigned a value of `1` if an error occurred or `0` if the error did not occur. The trailing number in each file name corresponds to the respective HumanEval-X Program (see [HumanEval-X](https://huggingface.co/datasets/THUDM/humaneval-x) for further details).

  - **Compilation Matrix Files**:
    - `compilation_matrix`: Captures the outcomes of translations (with `1` for success and `0` for failure).
    - `compilation_matrix_avg`: Contains the average success score for each translation pair.
    - `compilation_matrix_std_deviation`: Contains the standard deviation for each translation pair.

  - **Retanslation Experiments**  
    Folders with names appended by `_Number` (e.g., `_1`, `_2`, etc.) denote successive iterations performed during the retranslation experiments.

- **Preliminarystudys**  
  This folder contains early-stage studies based on a subset of problems, and the structure here differs slightly from that of the full dataset. Equivalent CSV files are also available in the `log` subdirectory.

  - **ErrorMessagesForRetranslation**: Holds detailed error messages that provide additional context for retranslation experiments.

- **Figures**  
  This directory includes visualizations generated for the paper. These figures illustrate various aspects such as:
  - **ErrorsPerProblem**: Shows the 10 programs with the highest number of errors.
  - **RelativeErrorDistribution**: Depicts the percentage distribution of errors observed during retranslation.
  - **CurveRemainingErrors**: Illustrates the decline of errors across successive retranslation iterations.
  - **Spider Charts**: Present error distributions with respect to both target and source languages.

- **Programms**  
  Contains the programs used in the translation experiments. Sources and explanations for the programs include:
  - **HelloWorld**: Derived from the resource provided by [GeeksforGeeks: Hello World in 30 Different Languages](https://www.geeksforgeeks.org/hello-world-in-30-different-languages/).
  - **SampleProgrammsinEveryLanguage**: Sourced from [SamplePrograms.io](https://sampleprograms.io/).
  - **HumanEval-X**: Provided by [HumanEval-X Dataset](https://huggingface.co/datasets/THUDM/humaneval-x), which includes further explanation of the programs.

- **Tables**  
  This folder contains tables with supplementary analytical data that further elaborate on the findings presented in the paper.

## Detailed Experiment Filenames and Descriptions

The experiments are organized by identifier and model combination. Each experiment uses a distinct setup to analyze the performance of code-to-code translation with various language models. Below is an explanation of the filenames for each experiment:

- **Experiment 5 / Quant1 = 1Turn GPT**  
  In this experiment, a one-turn translation is performed using GPT4o-mini. The experiment measures the translation accuracy in a single pass without iterative refinement. Results are captured in the corresponding CSV files under the Data directory.

- **Experiment 6 = Retranslate GPT**  
  This experiment involves retranslation with GPT4o-mini, where the initial translated code is retranslated iteratively. The goal is to analyze if and how retranslation improves the outcome or reduces error occurrences.

- **Experiment 7 = Explanation GPT**  
  In Experiment 7, GPT4o-mini is used to generate explanations for the translation results.

- **Experiment 13 = 1Turn Claude**  
  Similar to Experiment 5, this experiment conducts a one-turn translation using the Claude Sonnet 3.7 model. The single-pass translation is analyzed to assess the model’s translation success across language pairs.

- **Experiment 14 = Retranslate Claude**  
  This experiment applies iterative retranslation using the Claude Sonnet 3.7 model. The experiment is designed to compare whether multiple translation iterations with Claude can refine the translation quality and reduce errors.

- **Experiment 15 = Explanation Claude**  
  In this experiment, the Claude Sonnet 3.7 model generates explanations for the translation outcomes.



## How to Use This Repository


1. **Data Analysis:**  
   - Load the CSV files into data analysis tools (such as Python’s Pandas library) to explore the matrix data.  
     Each matrix cell indicates whether an error occurred (`1`) or not (`0`), providing a comprehensive overview of translation performance across language pairs.
   - Review the calculated metrics in the `compilation_matrix_avg` and `compilation_matrix_std_deviation` files to understand the overall translation success and variance.

2. **Visualization and Additional Studies:**  
   - Consult the `Figures` folder to examine graphical representations of the results, including error trends and language-specific distributions.
   - For insight into initial test cases and specific errors, review the contents of the `Preliminarystudys` and `ErrorMessagesForRetranslation` folders.
   - The `Tables` directory contains further contextual and detailed information supporting the conclusions in the paper.

3. **Exploring Source Programs:**  
   - The `Programms` folder includes all the source programs used for both translation and testing. Refer to the included links for additional context and explanations of these programs.

## Concluding Remarks

This repository is intended to provide a transparent and reproducible framework for our experiments on code-to-code translation with LLMs. We invite researchers, practitioners, and interested readers to explore the contents, perform independent analyses, and contribute to furthering this line of inquiry. For additional questions, comments, or contributions, please refer to the contact information in the main paper.

