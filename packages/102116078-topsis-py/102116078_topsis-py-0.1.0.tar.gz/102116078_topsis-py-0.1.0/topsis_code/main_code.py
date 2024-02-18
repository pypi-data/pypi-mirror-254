# Develop a command line python program to implement the Topsis.

import sys
import numpy as np
import pandas as pd

def read_input_file(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

def validate_input_data(data, weights, impacts):
    # Check if the input file contains three or more columns
    if data.shape[1] < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)

    # Check if weights, impacts, and columns count match
    if len(weights) != len(impacts) or len(weights) != (data.shape[1] - 1):
        print("Error: Number of weights, impacts, and columns must be the same.")
        print(f"Provided values:\n Weights: {weights} \n Impacts: {impacts} \n Data: {data.shape[1] - 1}")
        sys.exit(1)

    # Check if non-numeric values present in data
    if not data.iloc[:, 1:].applymap(np.isreal).all().all():
        print("Error: Non-numeric values found in the data.")
        sys.exit(1)

def parse_weights(weights_str):
    try:
        weights = np.array([float(w) for w in weights_str.split(',')])
        return weights
    except ValueError:
        print("Error: Invalid weights. Ensure they are comma-separated numbers.")
        sys.exit(1)

def parse_impacts(impacts_str):
    valid_impacts = {'+', '-'}
    impacts = impacts_str.split(',')

    if any(impact not in valid_impacts for impact in impacts):
        print("Error: Invalid impacts. Use '+' for maximization and '-' for minimization.")
        sys.exit(1)

    return np.array([1 if imp == '+' else -1 for imp in impacts])

def save_results(data, scores, rankings, result_file):
    try:
        result_data = pd.DataFrame(data)
        result_data['Topsis_Score'] = scores
        result_data['Ranking'] = rankings
        result_data.to_csv(result_file, index=False)
        print(f"Results saved to {result_file}")
    except Exception as e:
        print(f"Error saving results: {e}")
        sys.exit(1)


def topsis(data, weights, impacts):
    # Step 1: Normalize the decision matrix
    norm_matrix = data / np.linalg.norm(data, axis=0)

    # Step 2: Weighted normalized decision matrix
    weighted_matrix = norm_matrix * weights

    # Step 3: Ideal and Anti-Ideal solutions
    ideal_best = np.max(weighted_matrix, axis=0)
    ideal_worst = np.min(weighted_matrix, axis=0)

    # Step 4: Calculate the separation measures
    separation_best = np.linalg.norm(weighted_matrix - ideal_best, axis=1)
    separation_worst = np.linalg.norm(weighted_matrix - ideal_worst, axis=1)

    # Step 5: Calculate the relative closeness to the ideal solution
    performance_score = separation_worst / (separation_best + separation_worst)

    # Step 6: Rank the alternatives
    rankings = np.argsort(performance_score)[::-1]
    
    return (rankings + 1, performance_score)  # Adding 1 to make rankings start from 1

def save_results(data, scores, rankings, result_file):
    try:
        result_data = pd.DataFrame(data)
        result_data['Topsis_Score'] = scores
        result_data['Ranking'] = rankings
        result_data.to_csv(result_file, index=False)
        print(f"Results saved to {result_file}")
    except Exception as e:
        print(f"Error saving results: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 5:
        print("Usage: python program.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights_str = sys.argv[2]
    impacts_str = sys.argv[3]
    result_file = sys.argv[4]

    # Read input data
    data = read_input_file(input_file)

    # Parse weights and impacts
    weights = parse_weights(weights_str)
    impacts = parse_impacts(impacts_str)

    # Validate input data
    validate_input_data(data, weights, impacts)

    # Run Topsis
    rankings = topsis(data.iloc[:, 1:].values, weights, impacts)

    # Save results
    save_results(data.values, rankings[1], rankings[0], result_file)

if __name__ == "__main__":
    main()
