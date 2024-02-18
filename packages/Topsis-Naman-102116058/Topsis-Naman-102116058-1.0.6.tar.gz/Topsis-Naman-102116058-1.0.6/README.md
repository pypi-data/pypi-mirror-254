# Project Description
- for: Assignment-1(UCS654)
- Submitted by: Naman Bhargava
- Roll no: 102116058
- Group: 3CS10

# TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)

This Python script is designed to implement the TOPSIS methodology for multi-criteria decision-making. It takes as input a CSV file that includes a decision matrix, user-defined weights, and impact specifications. The script then calculates TOPSIS scores and produces a ranked outcome, offering insights into the decision-making process.

## Installation
```bash
pip install Topsis-Naman-102116058
```

## Usage

```bash
from Topsis_Naman_102116058.topsis import topsis 
input="data.csv"
weights="1,1,1,2,1"
impacts="+,+,-,+,-"
result="result.csv" 
topsis(input, weights, impacts, result)
```

OR 

You can use this package via command line as:
```bash
python -m Topsis_Naman_102116058.topsis [Input as .csv] [Weights as a string] [Impacts as a string] [Result as .csv]
```

- `Input`: Path to the CSV file containing the input data.
- `Weights`: Comma-separated weights for each criterion.
- `Impacts`: Comma-separated impact direction for each criterion (`+` for maximization, `-` for minimization).
- `Result`: Name of the file to save the TOPSIS results.

## Requirements

- Python 3
- pandas
- numpy

## Input File Format
The input data should be in a CSV format with the following structure:

 | Fund Name |   P1  |   P2  |  P3  |   P4  |   P5   |
|-----------|-------|-------|------|-------|--------|
|    M1     |  0.62 |  0.38 |  6.7 |  58.7 |  16.60 |
|    M2     |  0.93 |  0.86 |  5.5 |  47.9 |  13.80 |
|    M3     |  0.62 |  0.38 |  3.2 |  65.9 |  17.53 |
|    M4     |  0.76 |  0.58 |  3.4 |  38.4 |  10.79 |
|    M5     |  0.74 |  0.55 |  3.1 |  56.4 |  15.20 |
|    M6     |  0.80 |  0.64 |  4.2 |  41.8 |  11.86 |
|    M7     |  0.95 |  0.90 |  4.1 |  50.3 |  14.06 |
|    M8     |  0.82 |  0.67 |  3.7 |  37.6 |  10.70 |


## Output

The script generates a CSV file containing the TOPSIS score and rank for each object:

| Fund Name |   P1  |   P2  |  P3  |   P4  |   P5   | Topsis Score | Rank |
|-----------|-------|-------|------|-------|--------|--------------|------|
|    M1     |  0.62 |  0.38 |  6.7 |  58.7 |  16.6  |   0.3876     |  8.0 |
|    M2     |  0.93 |  0.86 |  5.5 |  47.9 |  13.8  |   0.5213     |  4.0 |
|    M3     |  0.62 |  0.38 |  3.2 |  65.9 |  17.53 |   0.5715     |  3.0 |
|    M4     |  0.76 |  0.58 |  3.4 |  38.4 |  10.79 |   0.4401     |  7.0 |
|    M5     |  0.74 |  0.55 |  3.1 |  56.4 |  15.2  |   0.5977     |  2.0 |
|    M6     |  0.8  |  0.64 |  4.2 |  41.8 |  11.86 |   0.4403     |  6.0 |
|    M7     |  0.95 |  0.9  |  4.1 |  50.3 |  14.06 |   0.6352     |  1.0 |
|    M8     |  0.82 |  0.67 |  3.7 |  37.6 |  10.7  |   0.4517     |  5.0 |




## Error Handling

- Display an error message if the input file is not found.
- Raise a ValueError if the number of weights, impacts, or columns in the decision matrix is incorrect.
- Raise a ValueError if the columns from the 2nd to the last do not contain numeric values.
- Display any unexpected errors that occur during execution.

## LICENSE

(c) 2024 Naman Bhargava

This project is licensed under the [MIT License](LICENSE).