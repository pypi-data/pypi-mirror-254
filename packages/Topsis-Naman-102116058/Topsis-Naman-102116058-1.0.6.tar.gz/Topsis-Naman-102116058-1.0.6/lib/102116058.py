import pandas as pd
import numpy as np
import csv
import sys

def main():
    if len(sys.argv) == 5:
        input_data = sys.argv[1]
        weights_input = sys.argv[2]
        impacts_input = sys.argv[3]
        output_file = sys.argv[4]
        perform_topsis(input_data, weights_input, impacts_input, output_file)
    else:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python topsis.py input_data.csv \"1,1,1,2\" \"+,+,-,+\" output_data.csv")

def perform_topsis(input_data, weights_input, impacts_input, output_file):
    try:
        data_frame = pd.read_csv(input_data)
        print(data_frame)

        if len(weights_input.split(',')) != len(data_frame.columns) - 1 or len(impacts_input.split(',')) != len(data_frame.columns) - 1:
            raise ValueError("Number of weights, impacts, and columns must be the same.")

        weights = [float(w) for w in weights_input.split(',')]
        impacts = [1 if i == '+' else 0 for i in impacts_input.split(',')]

        if not data_frame.iloc[:, 1:].applymap(lambda x: isinstance(x, (int, float))).all().all():
            raise ValueError("Columns from 2nd to last must contain numeric values only.")

        normalized_data_frame = data_frame.iloc[:, 1:] / np.sqrt((data_frame.iloc[:, 1:] ** 2).sum())

        weighted_normalized_data_frame = normalized_data_frame * weights
        print(weighted_normalized_data_frame)

        ideal_positive = (np.array(weighted_normalized_data_frame.max()) * np.array(impacts)) + (np.array(weighted_normalized_data_frame.min()) * (1 - np.array(impacts)))
        ideal_negative = (np.array(weighted_normalized_data_frame.max()) * (1 - np.array(impacts))) + (np.array(weighted_normalized_data_frame.min()) * (np.array(impacts)))

        separation_positive = ((weighted_normalized_data_frame - ideal_positive) ** 2).sum(axis=1) ** 0.5
        separation_negative = ((weighted_normalized_data_frame - ideal_negative) ** 2).sum(axis=1) ** 0.5

        topsis_score = separation_negative / (separation_negative + separation_positive)
        rank = topsis_score.rank(ascending=False)

        result_data_frame = pd.concat([data_frame, pd.DataFrame({'Topsis Score': topsis_score, 'Rank': rank})], axis=1)

        result_data_frame.to_csv(output_file, index=False, quoting=csv.QUOTE_ALL, quotechar='"')

        print(f"TOPSIS completed successfully. Result saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_data} not found.")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()

