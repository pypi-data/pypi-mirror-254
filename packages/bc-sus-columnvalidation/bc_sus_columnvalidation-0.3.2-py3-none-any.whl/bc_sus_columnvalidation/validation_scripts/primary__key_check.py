import pandas as pd

def primary_key_check(file_path, column):
    df = pd.read_excel(file_path)

    if len(column) == 1:
        return df[column[0]].is_unique()


    else:
        combined_keys = df[column]
        return combined_keys.duplicates().shape[0] == df.shape[0]