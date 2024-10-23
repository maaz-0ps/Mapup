import pandas as pd
import datetime

def calculate_time_based_toll_rates(unrolled_df_with_tolls):
    result_df = unrolled_df_with_tolls.copy()
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
    for _, row in result_df.groupby(['id_start', 'id_end']).iterrows():
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            start_time = datetime.datetime.combine(datetime.date.today(), datetime.time(0, 0))
            end_time = start_time + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)
            start_day = day
            end_day = day if start_time.weekday() != end_time.weekday() else 'Sunday'
            if day in weekday_discount_factors:
                for start_hour, end_hour, discount_factor in weekday_discount_factors[day]:
                    if start_time >= start_hour and start_time < end_hour:
                        result_df.loc[(result_df['id_start'] == row['id_start']) & (result_df['id_end'] == row['id_end']) & (result_df['start_day'] == start_day) & (result_df['end_day'] == end_day), ['moto', 'car', 'rv', 'bus', 'truck']] *= discount_factor
            else:
                result_df.loc[(result_df['id_start'] == row['id_start']) & (result_df['id_end'] == row['id_end']) & (result_df['start_day'] == start_day) & (result_df['end_day'] == end_day), ['moto', 'car', 'rv', 'bus', 'truck']] *= weekend_discount_factor

            start_time = end_time + datetime.timedelta(seconds=1)
            end_time += datetime.timedelta(days=1)
    result_df['start_day'] = start_day
    result_df['start_time'] = start_time.time()
    result_df['end_day'] = end_day
    result_df['end_time'] = end_time.time()

    return result_df