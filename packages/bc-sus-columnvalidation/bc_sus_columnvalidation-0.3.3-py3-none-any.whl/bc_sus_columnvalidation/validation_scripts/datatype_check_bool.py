import pandas as pd


def datatype_check_bool(column_df):
    # loading the file and basic file based error handling to be done
    

    def is_bool(value):
        # check first if the values are "True" or "False"
        
        
        if isinstance(value, bool):
            return True
        # if not then check if it is a string. It could be "true"/"false"
        # convert to lower and check
        if isinstance(value, str):
            return value.lower() in ["true", "false"]
        # everything else is a fail case
        return False

    non_missing_df = column_df.dropna()#drop empty values 
    # column_df = column_df == 1.0

    non_bool_mask = ~non_missing_df.apply(is_bool)

    non_bool_rows = non_missing_df[non_bool_mask]

    if non_bool_rows.empty:
        return True
    else:

        non_bool_row_numbers = non_bool_rows.index.tolist()
        non_bool_row_numbers = [x + 2 for x in non_bool_row_numbers]
        return {"no_of_rows_failed": len(non_bool_row_numbers), "rows_which_failed": non_bool_row_numbers}


if __name__ == "__main__":
    df = pd.read_excel("Seedling_Distribution_TEMPLATE (1) vera data.xlsx", sheet_name="Seedling Database")
    column_df = df["BC Farmer"]
    print(datatype_check_bool(column_df))