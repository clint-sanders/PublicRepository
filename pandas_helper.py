import pandas as pd

def printRow(list, maxlength_in_col, prefix, suffix):
    if(len(list) != len(maxlength_in_col)):
        print("BIG ERROR")
        return

    str_to_print = ""
    for i in range(len(list)):
        col_str = list[i]
        num_spaces = maxlength_in_col[i]-len(col_str)
        str_to_print += prefix
        str_to_print += col_str
        for j in range(num_spaces):
            str_to_print += " "
        str_to_print += suffix
    print(str_to_print)

def getMaxLenInCol(dataframe):
    rval = [0] * len(dataframe[0]) #list of zeros for every column
    for row in dataframe:
        for i in range(len(row)):
            if len(row[i]) > rval[i]:
                rval[i] = len(row[i])
    return rval

def trimRowLength(temp_data_frame, max_col_width):
    dotdotdot = "..."
    for row in range(len(temp_data_frame)):
        for col in range(len(temp_data_frame[row])):
            if len(temp_data_frame[row][col]) > max_col_width:
                temp_data_frame[row][col] = temp_data_frame[row][col][0:max_col_width] + dotdotdot

def getFormattedVal(val, dtype, float_precision):
    #Format based on type. Float has precision, strings have quotes
    if (str(dtype).lower()[:3] == "int"):
        return str(val)

    if (str(dtype).lower()[:5] == "float"):
        formatter = "%." + str(float_precision) + "f"
        return (formatter % val)

    #Surround value with quotes to see whitespace
    return "\""+str(val)+"\""

def printPandaHead(df, n=5, max_col_width=0, float_precision = 5, prefix = "| ", suffix=" "):
    temp_data_frame = []

    # put column names in temp_data_frame to print out
    temp_row = []  # reset temp row
    for col in df.columns:
        temp_row.append(col)
    temp_data_frame.append(temp_row)

    # put column types in temp_data_frame to print out
    temp_row = []#reset temp row
    for col in df.columns:
        temp_row.append(str(df[col].dtype))
    temp_data_frame.append(temp_row)

    #Count number of printed rows. quit when it reaches "n" number of rows
    rows_printed = 0
    for index, rows in df.iterrows():
        #stop after n number of rows
        if rows_printed >= n:
            break
        rows_printed += 1 #increase the count of the number or rows

        temp_row = []
        for col in df.columns:
            temp_row.append(getFormattedVal(rows[col], df[col].dtype, float_precision))
        temp_data_frame.append(temp_row)

    if(max_col_width > 0):
        trimRowLength(temp_data_frame, max_col_width)

    maxlength_in_col = getMaxLenInCol(temp_data_frame)
    for row in temp_data_frame:
        printRow(row, maxlength_in_col, prefix, suffix)

    print("Printed " + str(rows_printed) + " rows out of " + str(df.shape[0]))
