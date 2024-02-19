import pandas as pd


def datatype_check_bool(excel_file, sheet_name, column_name):
    # loading the file and basic file based error handling to be done
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name,
                           usecols=[column_name])
    except FileNotFoundError:
        return f"Error: {excel_file} does not exist."
    except Exception as e:
        return f"Error: Encountered while reading the file {e}"

    if column_name not in df:
        return f"Error: {column_name} not found in the sheet. Check and re-submit."
    # convert it into a series
    df_series = df[column_name]

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

    non_missing_df = df_series.dropna()#drop empty values 

    non_bool_mask = ~non_missing_df.apply(is_bool)

    non_bool_rows = non_missing_df[non_bool_mask]

    if non_bool_rows.empty:
        return True
    else:

        non_bool_row_numbers = non_bool_rows.index.tolist()
        non_bool_row_numbers = [x + 2 for x in non_bool_row_numbers]
        return {"no_of_rows_failed": len(non_bool_row_numbers), "rows_which_failed": non_bool_row_numbers}


if __name__ == "__main__":
    result = datatype_check_bool(
        "COH_Deliveries_TEMPLATE_22_23_Example_Data (1) (1).xlsx",
        "Unique_Farmers", "All declared are mapped")
    print(result)
