import pandas as pd
import os


def calculate_distance_matrix(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")


    df = pd.read_csv(file_path)
try:import pandas as pd

def unroll_distance_matrix(distance_matrix):
    unrolled_data = []
    for start, row in distance_matrix.iterrows():
        for end, distance in row.iteritems():
            if start != end and not pd.isnull(distance):
                unrolled_data.append((start, end, distance))
    unrolled_df = pd.DataFrame(unrolled_data, columns=['id_start', 'id_end', 'distance'])

    return unrolled_df
unrolled_df = unroll_distance_matrix(distance_matrix)
print(unrolled_df)
    file_path = 'dataset-2.csv'
    distance_matrix = calculate_distance_matrix(file_path)
    print(distance_matrix)
except FileNotFoundError as e:
    print(f"Error: {e}")