import pandas as pd
import datetime

def datatype_check_date(column_df):
   
    

    
    def datecheck(field):
        date_format = '%d-%m-%Y'
        if "/" in field:
           field = field.replace("/", "-")
        
        try:
            dateObject = datetime.datetime.strptime(field, date_format)
            return True
            
        except ValueError:
            return False

    
    column_df = column_df.astype(str)
    non_missing_df = column_df.dropna()

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

# if __name__ == "__main__":
#     df = pd.read_excel("Seedling_Distribution_TEMPLATE_sample.xlsx", sheet_name="Seedling Database",parse_dates=False)
#     column_df = df["Distribution Date"]
#     # print(column_df)
#     # column_df.to_csv("date_check.csv", index=False)
#     print(datatype_check_date(column_df))