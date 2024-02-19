import pandas as pd
import io

from .validation_scripts import (
    datatype_check_bool,
    datatype_check_integer,
    missing_data_check,
    # non_negative_check
)


class ExcelValidator:
    def __init__(self, excel_file, sheet_name):
        self.excel_file = excel_file
        self.sheet_name = sheet_name
        self.df = pd.read_excel(excel_file, sheet_name=sheet_name)

        # self.validation_comments = {
        #     "datatype_check_integer": "Entry has to be an integer {...-2, -1, 0, 1, 2,...}.",
        #     "datatype_check_bool": 'Entry has to be either "True" or "False".',
        #     "missing_data_check": "Entry should not be blank."
        # }

        self.check_functions = {
            "datatype_check_integer": datatype_check_integer,
            "datatype_check_bool": datatype_check_bool,
            "missing_data_check": missing_data_check,
            # "non_negative_check": non_negative_check,
        }

    def insert_validation_columns(self):
        self.df.insert(0, "Errors", "No")
        self.df.insert(1, "Checks Performed", "")

    def perform_checks(self, mapping):
        for column_name, checks in mapping.items():
            for check in checks:
                result = self._execute_check(check, column_name)
                self._update_df_with_results(column_name, check, result)

    def _execute_check(self, check, column_name):
        check_function = self.check_functions.get(check)
        if check_function:
            return check_function(self.excel_file, self.sheet_name, column_name)
        else:
            raise ValueError(f"Check Function for {check} not found. ")

    def _update_df_with_results(self, column_name, check, result):
        if isinstance(result, dict):
            for row in result["rows_which_failed"]:
                excel_row = row - 2
                self.df.at[excel_row, "Errors"] = "Yes"
                self.df.at[
                    excel_row, "Checks Performed"
                ] += f" [{column_name} - {check}];  "

    def cleanup_and_save(self, new_file_name):
        self.df["Errors"] = self.df["Errors"].str.rstrip(", ")
        self.df["Checks Performed"] = self.df["Checks Performed"].str.rstrip(
            ", ")

        # self.df.to_excel(
        #     new_file_name, sheet_name=self.sheet_name, index=False)

        #returning the excel file object as bytestream to be able to be served in azure blob storage            
        output = io.BytesIO()

        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            self.df.to_excel(writer)
            
        output.seek(0)

        return output







