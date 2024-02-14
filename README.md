# My public GitHub repository
## pandas_helper.py
### Functions for displaying pandas' dataframes:
### printPandaHead(df, n=5, max_col_width=0, float_precision=5, prefix="| ", suffix=" ")
* df - panda data frame.
* n - number of lines to display, or list of lines to display.
* max_col_width - when printing out columns, no column should exceed this width. Default of 0 means no max length.
* float_precision - floating point numbers will be printed with this many decimals of precision.
* prefix - a prefix string printed before each column. Useful for showing separation.
* suffix - like prefix, but the suffix.

Non-numerical columns will be surrounded by quotations marks "like so" - useful for seeing possible leading and trailing white-space.

Examples using census data of state name, population, and income  

n is 5, printing out the first 5 rows of the data frame (which is also the default). Float precision is default.  
`printPandaHead(census, n=5)`  
output of call:  
`| state        | totalpop | income      `  
`| object       | int64    | float64     `   
`| "Alabama"    | 4830620  | 43296.36000`  
`| "Alaska"     | 733375   | 70354.74000`  
`| "Arizona"    | 6641928  | 54207.82000`  
`| "Arkansas"   | 2958208  | 41935.63000`  
`| "California" | 38421464 | 67264.78000`  
`Printed 5 rows out of 51`  

n is list that contains the index of the first row and last row. Float precision is to one decimal  
`printPandaHead(census, n=[0,census.shape[0]-1], float_precision=1)`  
output of call:  
`| state       | totalpop | income `  
`| object      | int64    | float64`  
`| "Alabama"   | 4830620  | 43296.4`  
`| "Wisconsin" | 5742117  | 53898.9`  
`Printed 2 rows out of 51`  

