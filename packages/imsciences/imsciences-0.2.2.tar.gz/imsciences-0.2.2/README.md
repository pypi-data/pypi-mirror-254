The IMS package is a python library for processing incomming data into a format that we can use for projects. IMS processing comes with the ability to:

1. remove_rows_cols(df, number_of_rows, number_of_cols):

    This function takes in a data frame and number of rows that you wish to remove and returns a data frame with that number of rows and/or cols less

2. aggregate_to_wc(df, date_column, group_columns, sum_columns, wc):

    Aggregates daily data into weekly data, starting on either Sundays or Mondays as specified, 
    and groups the data by additional specified columns. It sums specified numeric columns, 
    and pivots the data to create separate columns for each combination of the group columns 
    and sum columns. NaN values are replaced with 0.

3. convert_monthly_to_daily(self, df, date_column)

    This function takes in a monthly df and we convert a value into daily data

4. plot_two(df1, col1, df2, col2)

    This function allows you to plot out two data frames extreamly useful for displaying overlap on old vs new processed data