import pandas as pd
import os


def calculate_distance_matrix(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")


    df = pd.read_csv(file_path)
try:
    file_path = 'dataset-2.csv'
    distance_matrix = calculate_distance_matrix(file_path)
    print(distance_matrix)
except FileNotFoundError as e:
    print(f"Error: {e}")