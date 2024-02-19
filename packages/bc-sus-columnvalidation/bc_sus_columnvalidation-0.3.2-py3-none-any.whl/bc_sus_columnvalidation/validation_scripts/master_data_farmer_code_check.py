import pandas as pd
master_data_farmer_code_list = [
    "ER/001/2/3-0004",
    "ER/001/2/3-0002",
    "ER/001/2/3-0003",
    "E4/401/2/3-0001",
    "ER/041/2/3-0006",
    "ER/001/2/3-0004",
    "ER/001/2/3-0004",
    "ER/004/2/3-0004",
    "ER/001/2/3-0004",
    "ER/001/2/5-0004",
    "ER/001/2/3-0004",
]

def master_data_farmer_code_check(excel_file, sheet_name, column_name):
   
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[column_name])
    except FileNotFoundError:
        return f"Error: {excel_file} does not exist."
    except Exception as e:
        return f"Error: Encountered while reading the file {e}"

    if column_name not in df:
        return f"Error: {column_name} not found in the sheet. Check and re-submit."

    df_series = df[column_name]

    def is_present_in_master_Data(value):
        if value in master_data_farmer_code_list:
            return True
        return False

    non_missing_df = df_series.dropna()

    wrong_farmer_code_mask = ~non_missing_df.apply(is_present_in_master_Data)
    # get a list as o/p with the datatype check result(True or false); invert it;
    #  filter the column with that mask and get the failed row indices alone



    wrong_farmer_code_rows = non_missing_df[wrong_farmer_code_mask]

    if wrong_farmer_code_rows.empty:
        return True
    wrong_farmer_code_row_numbers = wrong_farmer_code_rows.index.tolist()
    wrong_farmer_code_row_numbers = [x + 2 for x in wrong_farmer_code_row_numbers]
    return {
        "No of rows failed": len(wrong_farmer_code_row_numbers),
        "rows_which_failed": wrong_farmer_code_row_numbers,
    }
