# My public GitHub repository

## pandas_helper.py - functions for displaying pandas' dataframes.
### printPandaHead(df, n=5, max_col_width=0, float_precision=5, prefix="| ", suffix=" ")
* df - panda data frame
* n - number of lines to display, or list of lines to display
* max_col_width - when printing out columns, no column should exceed this width. Default of 0 means no max length.
* float_precision - floating point numbers will be printed with this many decimals of precision
* prefix - a prefix string printed before each column. Useful for showing separation
* suffix - like prefix, but the suffix 

Non-numerical columns will be surrounded by quotations marks "like so" - useful for seeing possible leading and trailing white-space.
