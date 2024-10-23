def flatten_dict(data, prefix=""):
  """Flattens a nested dictionary into a single level dictionary.

  Args:
    data: The nested dictionary to be flattened.
    prefix: The current prefix for the key (empty string initially).

  Returns:
    A dictionary with flattened keys and values.
  """

  flattened_dict = {}
  for key, value in data.items():
    new_key = f"{prefix}{key}" if prefix else key

    if isinstance(value, dict):
      # Recursively flatten sub-dictionaries
      flattened_dict.update(flatten_dict(value, f"{new_key}."))
    elif isinstance(value, list):
      # Handle lists by iterating through elements and adding index to key
      for i, item in enumerate(value):
        flattened_dict.update(flatten_dict(item, f"{new_key}[{i}]."))
    else:
      # Add simple key-value pairs
      flattened_dict[new_key] = value

  return flattened_dict

# Example usage
data = {
  "road": {
    "name": "Highway 1",
    "length": 350,
    "sections": [
      {
        "id": 1,
        "condition": {
          "pavement": "good",
          "traffic": "moderate"
        }
      }
    ]
  }
}

flattened_data = flatten_dict(data)
print(flattened_data)