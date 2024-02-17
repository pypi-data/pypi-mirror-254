import pandas as pd
import calendar
import os
import plotly.express as px
from datetime import datetime, timedelta

class dataprocessing:
    
    def help(self):
        print("This is the help section. The functions in the package are as follows:")

        print("\n0. get_wd_levels")
        print("   - Description: Get whoever is working file directory with the option of moving up parents.")
        print("   - Usage: get_wd_levels(levels)")
        print("   - Example: get_wd_levels(0)")

        print("\n1. remove_rows")
        print("   - Description: Removes a specified number of rows from a pandas DataFrame.")
        print("   - Usage: remove_rows(data_frame, num_rows_to_remove)")
        print("   - Example: remove_rows(df, 2)")

        print("\n2. aggregate_to_wc")
        print("   - Description: Aggregates daily data into weekly data, grouping and summing specified columns.")
        print("   - Usage: aggregate_to_wc(df, date_column, group_columns, sum_columns, wc)")
        print("   - Example: aggregate_to_wc(df, 'date', ['platform'], ['cost', 'impressions', 'clicks'], 'mon')")

        print("\n3. convert_monthly_to_daily")
        print("   - Description: Converts monthly data in a DataFrame to daily data by expanding and dividing the numeric values.")
        print("   - Usage: convert_monthly_to_daily(df, date_column)")
        print("   - Example: convert_monthly_to_daily(df, 'date')")

        print("\n4. plot_two")
        print("   - Description: Plots specified columns from two different DataFrames using a shared date column. Excellent for comparing new and old data.")
        print("   - Usage: plot_two(df1, col1, df2, col2, date_column)")
        print("   - Example: plot_two(df1, 'cost', df2, 'cost', 'obs')")

        print("\n5. remove_nan_rows")
        print("   - Description: Removes rows from a DataFrame where the specified column has NaN values.")
        print("   - Usage: remove_nan_rows(df, col_to_remove_rows)")
        print("   - Example: remove_nan_rows(df, 'date')")

        print("\n6. filter_rows")
        print("   - Description: Filters the DataFrame based on whether the values in a specified column are in a provided list.")
        print("   - Usage: filter_rows(df, col_to_filter, list_of_filters)")
        print("   - Example: filter_rows(df, 'country', ['UK', 'IE'])")

        print("\n7. plot_one")
        print("   - Description: Plots specified columns from one DataFrames.")
        print("   - Usage: plot_one(df1, col1, date_column)")
        print("   - Example: plot_one(df, 'Spend', 'OBS')")

        print("\n8. convert_weekly_to_date")
        print("   - Description: Takes in a week col in format yyyy-'w'ww or yyyy-ww and converts it to wc.")
        print("   - Usage: convert_weekly_to_date(df, column_name, first_week_start_date)")
        print("   - Example: convert_weekly_to_date(df, 'week', '30/12/2019')")

        print("\n9. exclude_rows")
        print("   - Description: Remove rows from a df")
        print("   - Usage: exclude_rows(self, df, col_to_filter, list_of_filters)")
        print("   - Example: exclude_rows(df, 'week', ['2022-W20', '2022-W21'])")

    def get_wd_levels(self, levels):
        directory = os.getcwd()
        for _ in range(levels):
            directory = os.path.dirname(directory)
        return directory

    def remove_rows(self, data_frame, num_rows_to_remove):
        """
        Removes the specified number of rows from the given data frame, including the top row containing column names. 
        The next row will be treated as the new set of column headings.

        Parameters:
        - data_frame: pandas DataFrame
            The input data frame.
        - num_rows_to_remove: int
            The number of rows to remove from the data frame, starting from the original header.

        Returns:
        - pandas DataFrame
            The modified data frame with rows removed and new column headings.

        Raises:
        - TypeError: If num_rows_to_remove is not an integer.
        - ValueError: If num_rows_to_remove is negative or exceeds the total number of rows.
        """
        
        if not isinstance(num_rows_to_remove, int):
            raise TypeError("num_rows_to_remove must be an integer")

        if num_rows_to_remove < 0 or num_rows_to_remove >= len(data_frame):
            raise ValueError("Number of rows to remove must be non-negative and less than the total number of rows in the data frame.")

        if num_rows_to_remove == 0:
            return data_frame

        new_header = data_frame.iloc[num_rows_to_remove - 1]
        modified_data_frame = data_frame[num_rows_to_remove:] 
        modified_data_frame.columns = new_header

        return modified_data_frame
    
    def aggregate_to_wc(self, df, date_column, group_columns, sum_columns, wc):
        """
        Aggregates daily data into weekly data, starting on a specified day of the week, 
        and groups the data by additional specified columns. It sums specified numeric columns, 
        and pivots the data to create separate columns for each combination of the group columns 
        and sum columns. NaN values are replaced with 0 and the index is reset. The day column 
        is renamed from 'Day' to 'OBS'.

        Parameters:
        - df: pandas DataFrame
            The input DataFrame containing daily data.
        - date_column: string
            The name of the column in the DataFrame that contains date information.
        - group_columns: list of strings
            Additional column names to group by along with the weekly grouping.
        - sum_columns: list of strings
            Numeric column names to be summed during aggregation.
        - wc: string
            The week commencing day (e.g., 'sun' for Sunday, 'mon' for Monday).

        Returns:
        - pandas DataFrame
            A new DataFrame with weekly aggregated data. The index is reset,
            and columns represent the grouped and summed metrics. The DataFrame 
            is in wide format, with separate columns for each combination of 
            grouped metrics.
        """
        
        # Map the input week commencing day to a weekday number (0=Monday, 6=Sunday)
        days = {'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3, 'fri': 4, 'sat': 5, 'sun': 6}
        if wc.lower() not in days:
            return print(f"Incorrect week commencing day input: '{wc}'. Please choose a valid day of the week (e.g., 'sun', 'mon', etc.).")

        start_day = days[wc.lower()]

        # Make a copy of the DataFrame
        df_copy = df.copy()

        # Convert the date column to datetime
        df_copy[date_column] = pd.to_datetime(df_copy[date_column])

        # Determine the start of each week
        df_copy['week_start'] = df_copy[date_column].apply(lambda x: x - pd.Timedelta(days=(x.weekday() - start_day) % 7))

        # Convert sum_columns to numeric and fill NaNs with 0
        for col in sum_columns:
            df_copy[col] = pd.to_numeric(df_copy[col], errors='coerce').fillna(0).astype(int)

        # Group by the new week start column and additional columns, then sum the numeric columns
        grouped = df_copy.groupby(['week_start'] + group_columns)[sum_columns].sum().reset_index()

        # Rename 'week_start' column to 'OBS'
        grouped = grouped.rename(columns={'week_start': 'OBS'})

        # Pivot the data to wide format
        if group_columns:
            wide_df = grouped.pivot_table(index='OBS', 
                                        columns=group_columns, 
                                        values=sum_columns,
                                        aggfunc='first')
            # Flatten the multi-level column index and create combined column names
            wide_df.columns = [' '.join(col).strip() for col in wide_df.columns.values]
        else:
            wide_df = grouped.set_index('OBS')

        # Fill NaN values with 0
        wide_df = wide_df.fillna(0)

        # Adding total columns for each unique sum_column
        for col in sum_columns:
            total_column_name = f'Total {col}'
            if group_columns:
                # Columns to sum for each unique sum_column when group_columns is provided
                columns_to_sum = [column for column in wide_df.columns if col in column]
            else:
                # When no group_columns, the column itself is the one to sum
                columns_to_sum = [col]
            wide_df[total_column_name] = wide_df[columns_to_sum].sum(axis=1)

        # Reset the index of the final DataFrame
        wide_df = wide_df.reset_index()

        return wide_df
        
    def convert_monthly_to_daily(self, df, date_column):
        """
        Convert a DataFrame with monthly data to daily data.
        This function takes a DataFrame and a date column, then it expands each
        monthly record into daily records by dividing the numeric values by the number of days in that month.

        :param df: DataFrame with monthly data.
        :param date_column: The name of the column containing the date.
        :return: A new DataFrame with daily data.
        """

        # Convert date_column to datetime
        df[date_column] = pd.to_datetime(df[date_column])

        # Initialize an empty list to hold the daily records
        daily_records = []

        # Iterate over each row in the DataFrame
        for _, row in df.iterrows():
            # Calculate the number of days in the month
            num_days = calendar.monthrange(row[date_column].year, row[date_column].month)[1]

            # Create a new record for each day of the month
            for day in range(1, num_days + 1):
                daily_row = row.copy()
                daily_row[date_column] = row[date_column].replace(day=day)

                # Divide each numeric value by the number of days in the month
                for col in df.columns:
                    if pd.api.types.is_numeric_dtype(df[col]) and col != date_column:
                        daily_row[col] = row[col] / num_days

                daily_records.append(daily_row)

        # Convert the list of daily records into a DataFrame
        daily_df = pd.DataFrame(daily_records)
        
        return daily_df
    
    def plot_two(self, df1, col1, df2, col2, date_column):
        """
        Plots specified columns from two different dataframes with white background and black axes,
        using a specified date column as the X-axis.

        :param df1: First DataFrame
        :param col1: Column name from the first DataFrame
        :param df2: Second DataFrame
        :param col2: Column name from the second DataFrame
        :param date_column: The name of the date column to use for the X-axis
        """

        # Check if columns exist in their respective dataframes
        if col1 not in df1.columns or col2 not in df2.columns or date_column not in df1.columns or date_column not in df2.columns:
            raise ValueError("Column not found in respective DataFrame")

        # Check if the date column is in datetime format, if not convert it
        df1[date_column] = pd.to_datetime(df1[date_column])
        df2[date_column] = pd.to_datetime(df2[date_column])

        # Merge the two dataframes on the date column
        merged_df = pd.merge(df1[[date_column, col1]], df2[[date_column, col2]], on=date_column, how='outer')

        # Rename the columns to ensure they are unique
        col1_new = col1 + ' (df1)'
        col2_new = col2 + ' (df2)'

        merged_df.rename(columns={col1: col1_new, col2: col2_new}, inplace=True)

        # Plotting using Plotly Express
        fig = px.line(merged_df, x=date_column, y=[col1_new, col2_new])

        # Update layout for white background and black axes lines, and setting y-axis to start at 0
        fig.update_layout(
            plot_bgcolor='white',
            xaxis=dict(
                showline=True,
                linecolor='black'
            ),
            yaxis=dict(
                showline=True,
                linecolor='black',
                rangemode='tozero'  # Setting Y-axis to start at 0
            )
        )

        return fig

    def remove_nan_rows(self, df, col_to_remove_rows):
    # This line drops rows where the specified column has NaN values
        return df.dropna(subset=[col_to_remove_rows])
    
    def filter_rows(self, df, col_to_filter, list_of_filters):
    # This line filters the DataFrame based on whether the values in the specified column are in the list_of_filters
        return df[df[col_to_filter].isin(list_of_filters)]
    
    def plot_one(self, df1, col1, date_column):
        """
        Plots specified column from a DataFrame with white background and black axes,
        using a specified date column as the X-axis.

        :param df1: DataFrame
        :param col1: Column name from the DataFrame
        :param date_column: The name of the date column to use for the X-axis
        """

        # Check if columns exist in the DataFrame
        if col1 not in df1.columns or date_column not in df1.columns:
            raise ValueError("Column not found in DataFrame")

        # Check if the date column is in datetime format, if not convert it
        if not pd.api.types.is_datetime64_any_dtype(df1[date_column]):
            df1[date_column] = pd.to_datetime(df1[date_column])

        # Plotting using Plotly Express
        fig = px.line(df1, x=date_column, y=col1)

        # Update layout for white background and black axes lines, and setting y-axis to start at 0
        fig.update_layout(
            plot_bgcolor='white',
            xaxis=dict(
                showline=True,
                linecolor='black'
            ),
            yaxis=dict(
                showline=True,
                linecolor='black',
                rangemode='tozero'  # Setting Y-axis to start at 0 if suitable
            )
        )

        return fig

    def convert_weekly_to_date(self, df, column_name, first_week_start_date):
        def get_week_start_date(week_code):
            parts = week_code.split('-')
            year = int(parts[0])
            
            # Check if week part contains 'W' and extract week number accordingly
            week_part = parts[1]
            week_num = int(week_part[1:]) if 'W' in week_part else int(week_part)
            
            first_week_start = datetime.strptime(first_week_start_date, '%d/%m/%Y')
            week_start_date = first_week_start + timedelta(weeks=week_num - 1)
            return week_start_date.strftime('%d/%m/%Y')
        
        # Create a mapping of week codes to dates
        unique_weeks = df[column_name].unique()
        week_to_date_mapping = {week: get_week_start_date(week) for week in unique_weeks}

        # Map each row in the DataFrame to the corresponding date
        df[f'{column_name}_start_date'] = df[column_name].map(week_to_date_mapping)

        return df
    
    def exclude_rows(self, df, col_to_filter, list_of_filters):
        # This line filters the DataFrame based on whether the values in the specified column are not in the list_of_filters
        return df[~df[col_to_filter].isin(list_of_filters)]