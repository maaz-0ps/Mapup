import pandas as pd

def calculate_distance_matrix(file_path):
    """
    Calculates a distance matrix based on the given CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The distance matrix.
    """

    # Load the CSV data into a DataFrame
    df = pd.read_csv(file_path)

    # Create a unique list of toll locations
    toll_locations = df['Toll Location'].unique()

    # Create an empty distance matrix
    distance_matrix = pd.DataFrame(index=toll_locations, columns=toll_locations)

    # Fill the distance matrix with known distances
    for index, row in df.iterrows():
        start = row['Toll Location']
        end = row['Next Toll Location']
        distance = row['Distance']

        distance_matrix.loc[start, end] = distance
        distance_matrix.loc[end, start] = distance

    # Fill in missing distances using cumulative sums
    for start in toll_locations:
        for end in toll_locations:
            if start != end and pd.isnull(distance_matrix.loc[start, end]):
                for intermediate in toll_locations:
                    if not pd.isnull(distance_matrix.loc[start, intermediate]) and not pd.isnull(distance_matrix.loc[intermediate, end]):
                        distance_matrix.loc[start, end] = distance_matrix.loc[start, intermediate] + distance_matrix.loc[intermediate, end]
                        break

    # Set diagonal values to 0
    distance_matrix.values.fill_diagonal(0)

    return distance_matrix

# Example usage:
file_path = 'dataset-2.csv'
distance_matrix = calculate_distance_matrix(file_path)
print(distance_matrix)