import pandas as pd


def datatype_check_integer(excel_file, sheet_name, column_name):
   
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[column_name])
    except FileNotFoundError:
        return f"Error: {excel_file} does not exist."
    except Exception as e:
        return f"Error: Encountered while reading the file {e}"

    if column_name not in df:
        return f"Error: {column_name} not found in the sheet. Check and re-submit."

    df_series = df[column_name]

    def is_integer(value):
        try:
            return float(value).is_integer()
        except ValueError:
            return False

    non_missing_df = df_series.dropna()

    non_integer_mask = ~non_missing_df.apply(is_integer)
    # get a list as o/p with the datatype check result(True or false); invert it;
    #  filter the column with that mask and get the failed row indices alone

    non_integer_rows = non_missing_df[non_integer_mask]

    if non_integer_rows.empty:
        return True
    non_integer_row_numbers = non_integer_rows.index.tolist()
    non_integer_row_numbers = [x + 2 for x in non_integer_row_numbers]
    return {
        "No of rows failed": len(non_integer_row_numbers),
        "rows_which_failed": non_integer_row_numbers,
    }


if __name__ == "__main__":
    result = datatype_check_integer(
        "COH_Deliveries_TEMPLATE_22_23_Example_Data (1) (1).xlsx",
        "Unique_Farmers",
        "COH delivered volume in KG",
    )
    print(result)
