import pandas as pd
import datetime

def calculate_time_based_toll_rates(unrolled_df_with_tolls):
    """
    Calculates time-based toll rates for different time intervals within a day.

    Args:
        unrolled_df_with_tolls (pandas.DataFrame): The unrolled distance matrix with toll rates.

    Returns:
        pandas.DataFrame: The unrolled distance matrix with added time-based toll rate columns.
    """

    # Create a new DataFrame to store the results
    result_df = unrolled_df_with_tolls.copy()

    # Define time ranges and discount factors
    time_ranges = [
        (datetime.time(0, 0), datetime.time(10, 0), 0.8),
        (datetime.time(10, 0), datetime.time(18, 0), 1.2),
        (datetime.time(18, 0), datetime.time(23, 59, 59), 0.8)
    ]
    weekday_discount_factors = {
        'Monday': time_ranges,
        'Tuesday': time_ranges,
        'Wednesday': time_ranges,
        'Thursday': time_ranges,
        'Friday': time_ranges
    }
    weekend_discount_factor = 0.7

    # Calculate time-based toll rates for each unique (id_start, id_end) pair
    for _, row in result_df.groupby(['id_start', 'id_end']).iterrows():
        # Iterate over days of the week
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            # Calculate start and end times based on the day
            start_time = datetime.datetime.combine(datetime.date.today(), datetime.time(0, 0))
            end_time = start_time + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)
            start_day = day
            end_day = day if start_time.weekday() != end_time.weekday() else 'Sunday'

            # Apply discount factors based on time ranges
            if day in weekday_discount_factors:
                for start_hour, end_hour, discount_factor in weekday_discount_factors[day]:
                    if start_time >= start_hour and start_time < end_hour:
                        result_df.loc[(result_df['id_start'] == row['id_start']) & (result_df['id_end'] == row['id_end']) & (result_df['start_day'] == start_day) & (result_df['end_day'] == end_day), ['moto', 'car', 'rv', 'bus', 'truck']] *= discount_factor
            else:
                result_df.loc[(result_df['id_start'] == row['id_start']) & (result_df['id_end'] == row['id_end']) & (result_df['start_day'] == start_day) & (result_df['end_day'] == end_day), ['moto', 'car', 'rv', 'bus', 'truck']] *= weekend_discount_factor

            # Update start and end times for the next day
            start_time = end_time + datetime.timedelta(seconds=1)
            end_time += datetime.timedelta(days=1)

    # Add start_day, start_time, end_day, and end_time columns
    result_df['start_day'] = start_day
    result_df['start_time'] = start_time.time()
    result_df['end_day'] = end_day
    result_df['end_time'] = end_time.time()

    return result_df