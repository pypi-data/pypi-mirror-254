"""
This the exhaustive list of value restriction checks we need to perform
Certification
Currency
Tree Species
Project
Labor Group Activities
Labor Group Activity Status
Graduation Exam Answers
CL Identification
Countries
"""

import pandas as pd


# #below are the value restriction data that need to be sourced from google sheets
# certifications_list = [
#    "COCOA HORIZONS", 
#     "COCOA LIFE",
#     "FAIRTRADE",
#     "FERMICOA", 
#     "NCP",
#     "Not Certified",
#     "ORGANICO",
#     "RAINFOREST ALLIANCE",
#     "STARBUCKS",
#     "UTZ"
# ]

# projects_list = [
#     "HERSHEYS",
#     "MONDELEZ",
#     "COH",
#     "HOTEL CHOCOLAT",
#     "MARS",
#     "NESTLE",
#     "B&J",
#     "BARRY",
#     "UNILEVER",
#     "TRACE"
# ]


countries_list = [
    "SACO",
    "TT",
    "SUC",
    "ETG",
    "LTP",
    "GH",
    "CM",
    "ID",
    "BR",
    "EC",
    "NG",
]

def countries_value_restriction_check(excel_file, sheet_name, column_name):
   
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[column_name])
    except FileNotFoundError:
        return f"Error: {excel_file} does not exist."
    except Exception as e:
        return f"Error: Encountered while reading the file {e}"

    if column_name not in df:
        return f"Error: {column_name} not found in the sheet. Check and re-submit."

    df_series = df[column_name]

    def is_value_within_country_list(value):
        if value.upper().strip() in countries_list:
            return True
        return False

    non_missing_df = df_series.dropna()

    wrong_country_mask = ~non_missing_df.apply(is_value_within_country_list)
    # get a list as o/p with the datatype check result(True or false); invert it;
    #  filter the column with that mask and get the failed row indices alone



    wrong_country_rows = non_missing_df[wrong_country_mask]

    if wrong_country_rows.empty:
        return True
    wrong_country_row_numbers = wrong_country_rows.index.tolist()
    wrong_country_row_numbers = [x + 2 for x in wrong_country_row_numbers]
    return {
        "No of rows failed": len(wrong_country_row_numbers),
        "rows_which_failed": wrong_country_row_numbers,
    }


