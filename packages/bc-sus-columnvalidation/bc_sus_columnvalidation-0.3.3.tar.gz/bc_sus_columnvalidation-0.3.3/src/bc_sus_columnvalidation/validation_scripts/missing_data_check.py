# entry should not be blank is the check

import pandas as pd


def missing_data_check(column_df):

    
    missing_data = column_df.isnull()

    if missing_data.any():

        missing_rows = missing_data[missing_data].index.tolist()

        missing_count = missing_data.sum()
        
        missing_rows = [x + 2 for x in missing_rows]

        return {"no of rows missing": missing_count,
                "rows_which_failed": missing_rows
                } 
             
    else:
        return True


if __name__ == "__main__":
    print(
        missing_data_check(
            "COH_Deliveries_TEMPLATE_22_23_Example_Data (1) (1).xlsx",
            "Unique_Farmers", "Farmer Group Code"))
