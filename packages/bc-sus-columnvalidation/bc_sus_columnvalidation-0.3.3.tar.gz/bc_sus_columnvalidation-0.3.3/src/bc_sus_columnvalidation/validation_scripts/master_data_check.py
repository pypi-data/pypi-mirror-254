import pandas as pd


def master_data_check(master_data_column_df,column_df):

    



    is_in_master_data_df = column_df.isin(master_data_column_df)

    is_in_master_data_df = is_in_master_data_df.dropna()

    failed_master_data_check_rows = is_in_master_data_df[~is_in_master_data_df].index.tolist(
    )

    if len(failed_master_data_check_rows) == 0:
        return True
    wrong_master_data_rows = failed_master_data_check_rows
    wrong_master_data_rows = [x + 2 for x in wrong_master_data_rows]
    return {
        "No of rows failed": len(wrong_master_data_rows),
        "rows_which_failed": wrong_master_data_rows,
        # "total rows": len(master_data_column_df)
    }
