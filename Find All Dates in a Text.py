import polyline
import pandas as pd
import math

def decode_polyline_to_df(polyline_str):
  """Decodes a polyline string into a Pandas DataFrame with latitude, longitude, and distance.

  Args:
    polyline_str: The polyline string to decode.

  Returns:
    A Pandas DataFrame with latitude, longitude, and distance columns.
  """

  # Decode the polyline string into a list of coordinates
  coordinates = polyline.decode(polyline_str)

  # Create a Pandas DataFrame from the coordinates
  df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])

  # Calculate the distance between consecutive points using the Haversine formula
  def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Calculate the differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Calculate the Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371000  # Earth radius in meters
    return c * r

  df['distance'] = 0  # Initialize distance for the first row
  for i in range(1, len(df)):
    df.loc[i, 'distance'] = haversine_distance(df.loc[i - 1, 'latitude'], df.loc[i - 1, 'longitude'], df.loc[i, 'latitude'], df.loc[i, 'longitude'])

  return df

# Example usage
polyline_str = "a~|$AU|B~|$AU|C~|$AU|D~|$AU|E"
df = decode_polyline_to_df(polyline_str)
print(df)