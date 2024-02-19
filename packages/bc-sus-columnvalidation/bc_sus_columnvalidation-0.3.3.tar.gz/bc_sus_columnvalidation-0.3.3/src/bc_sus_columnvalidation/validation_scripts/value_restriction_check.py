import pandas as pd


def value_restriction_check(value_restriction_column_df, column_df):

   # TODO make sure we take into account non str value in Vlaue restrictions
    value_restriction_column_df = value_restriction_column_df.str.lower()
    column_df = column_df.str.lower()
    is_in_lookup_df = column_df.isin(value_restriction_column_df)

    is_in_lookup_df = is_in_lookup_df.dropna()

    failed_value_restriction_check_rows = is_in_lookup_df[~is_in_lookup_df].index.tolist(
    )

    if len(failed_value_restriction_check_rows) == 0:
        return True
    wrong_value_restriction_check = failed_value_restriction_check_rows
    wrong_value_restriction_check = [x + 2 for x in wrong_value_restriction_check]
    return {
        "No of rows failed": len(wrong_value_restriction_check),
        "rows_which_failed": wrong_value_restriction_check,
    }

    