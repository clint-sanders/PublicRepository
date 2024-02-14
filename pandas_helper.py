import pandas as pd

# print columns, datatype, then rows of dataframe. "n" can be a list of integers that index the rows of the dataframe
def printPandaHead(df, n=5, max_col_width=0, float_precision=5, prefix="| ", suffix=" "):
    temp_data_frame = []
    #n is a list of row numbers. A single int should be interpreted as printing the first n rows.
    if isinstance(n, int):
        n = range(n)
    # put column names in temp_data_frame to print out
    temp_data_frame.append(df.columns)
    # put column types in temp_data_frame to print out
    temp_data_frame.append([str(df[col].dtype) for col in df.columns])
    # Count number of printed rows.
    rows_printed = 0
    for i in n:
        # i index must be inside dataframe
        if i < 0 or i >= df.shape[0]:
            break
        rows = df.iloc[i]
        temp_data_frame.append([getFormattedVal(rows[col], df[col].dtype, float_precision) for col in df.columns])
        rows_printed += 1
    #if a max_col_width is given, trim to that width
    if (max_col_width > 0):
        trimRowWidth(temp_data_frame, max_col_width)
    #Find the width of the longest string in each column to align them vertically
    maxlength_in_col = getMaxWidthInCol(temp_data_frame)
    for row in temp_data_frame:
        printRow(row, maxlength_in_col, prefix, suffix)

    print("Printed " + str(rows_printed) + " rows out of " + str(df.shape[0]))

def printRow(list, maxlength_in_col, prefix, suffix):
    if (len(list) != len(maxlength_in_col)):
        print("BIG ERROR")
        return

    str_to_print = ""
    for i in range(len(list)):
        str_to_print += prefix
        col_str = list[i]
        num_spaces = maxlength_in_col[i] - len(col_str)
        str_to_print += col_str
        for j in range(num_spaces):
            str_to_print += " "
        str_to_print += suffix
    print(str_to_print)


def getMaxWidthInCol(dataframe):
    rval = [0] * len(dataframe[0])  # list of zeros for every column
    for row in dataframe:
        for i in range(len(row)):
            if len(row[i]) > rval[i]:
                rval[i] = len(row[i])
    return rval


def trimRowWidth(temp_data_frame, max_col_width):
    #dotdotdot adds to width, but gives visual indicator that the row was truncated
    dotdotdot = "..."
    for row in range(len(temp_data_frame)):
        for col in range(len(temp_data_frame[row])):
            if len(temp_data_frame[row][col]) > max_col_width:
                temp_data_frame[row][col] = temp_data_frame[row][col][0:max_col_width] + dotdotdot

def getFormattedVal(val, dtype, float_precision):
    # Format based on type. Float has precision, strings have quotes
    if (str(dtype).lower()[:3] == "int"):
        return str(val)

    if (str(dtype).lower()[:5] == "float"):
        formatter = "%." + str(float_precision) + "f"
        return (formatter % val)

    # Surround value with quotes to see whitespace
    return "\"" + str(val) + "\""
