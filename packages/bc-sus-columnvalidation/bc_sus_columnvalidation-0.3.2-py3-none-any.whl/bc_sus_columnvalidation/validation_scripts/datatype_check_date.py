import pandas as pd
import datetime

def datatype_check_date(excel_file, sheet_name, column_name):
   
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[column_name])
    except FileNotFoundError:
        return f"Error: {excel_file} does not exist."
    except Exception as e:
        return f"Error: Encountered while reading the file {e}"

    if column_name not in df:
        return f"Error: {column_name} not found in the sheet. Check and re-submit."

    df_series = df[column_name]

    
    def datecheck(field):
        date_format = '%d-%m-%Y'
        if "/" in field:
           field = field.replace("/", "-")
        
        try:
            dateObject = datetime.datetime.strptime(field, date_format)
            return True
            
        except ValueError:
            return False

    non_missing_df = df_series.dropna()

    wrong_date_mask = ~non_missing_df.apply(datecheck)
    # get a list as o/p with the datatype check result(True or false); invert it;
    #  filter the column with that mask and get the failed row indices alone



    wrong_date_rows = non_missing_df[wrong_date_mask]

    if wrong_date_rows.empty:
        return True
    wrong_date_row_numbers = wrong_date_rows.index.tolist()
    wrong_date_row_numbers = [x + 2 for x in wrong_date_row_numbers]
    return {
        "No of rows failed": len(wrong_date_row_numbers),
        "rows_which_failed": wrong_date_row_numbers,
    }