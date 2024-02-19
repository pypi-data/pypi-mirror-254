import pandas as pd

certifications_list = [
   "COCOA HORIZONS", 
    "COCOA LIFE",
    "FAIRTRADE",
    "FERMICOA", 
    "NCP",
    "Not Certified",
    "ORGANICO",
    "RAINFOREST ALLIANCE",
    "STARBUCKS",
    "UTZ"
]

def certifications_value_restriction_check(excel_file, sheet_name, column_name):
   
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[column_name])
    except FileNotFoundError:
        return f"Error: {excel_file} does not exist."
    except Exception as e:
        return f"Error: Encountered while reading the file {e}"

    if column_name not in df:
        return f"Error: {column_name} not found in the sheet. Check and re-submit."

    df_series = df[column_name]

    def is_value_within_certifications_list(value):
        if value.upper().strip() in certifications_list:
            return True
        return False

    non_missing_df = df_series.dropna()

    wrong_certification_mask = ~non_missing_df.apply(is_value_within_certifications_list)
    # get a list as o/p with the datatype check result(True or false); invert it;
    #  filter the column with that mask and get the failed row indices alone



    wrong_certifications_rows = non_missing_df[wrong_certification_mask]

    if wrong_certifications_rows.empty:
        return True
    wrong_certifications_row_numbers = wrong_certifications_rows.index.tolist()
    wrong_certifications_row_numbers = [x + 2 for x in wrong_certifications_row_numbers]
    return {
        "No of rows failed": len(wrong_certifications_row_numbers),
        "rows_which_failed": wrong_certifications_row_numbers,
    }

