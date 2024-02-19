import pandas as pd
pd.set_option('display.max_columns', None)
test_list = [
    ('Seedling Database', 'BC Farmer', 'Data Type Check', 'Boolean', None, None, 'Entry has to be either "True" or "False".'), 
    ('Seedling Database', 'BC Farmer', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Certification', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Certification', 'Value Restriction Check', None, 'Certifications', 'Certification', 'The value should be from the existing certifications list. Refer "Template Upload Portal - Overview" file.'), 
    ('Seedling Database', 'Country', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Country', 'Value Restriction Check', None, 'Countries', 'Countries', 'The value should be from the existing Countries list. Refer "Template Upload Portal - Overview" file.'), 
    ('Seedling Database', 'Distribution Date', 'Data Type Check', 'Date', None, None, 'Entry has to be a date of format DD/MM/YYYY.'), 
    ('Seedling Database', 'Distribution Date', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Farmer Code', 'Master Data Check', None, 'ZFarmerSnap', 'FARMER_CODE', 'Farmer code has to be in line with farmer code in our sustainability database.'), 
    ('Seedling Database', 'Farmer Code', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Farmer Code;Distribution Date;Tree Species', 'Primary Key Check', None, None, None, 'Each row should contain a unique value. If the primary key is a combination of two or more columns, make sure the combination serves as a unique identifier.'), 
    ('Seedling Database', 'Number of Seedlings', 'Data Type Check', 'Integer', None, None, 'Entry has to be an integer {...-2, -1, 0, 1, 2,...}.'), 
    ('Seedling Database', 'Number of Seedlings', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'PES agroforestry program', 'Data Type Check', 'Boolean', None, None, 'Entry has to be either "True" or "False".'), 
    ('Seedling Database', 'PES agroforestry program', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Project', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Project', 'Value Restriction Check', None, 'Projects', 'Project', 'The value should be from the existing projects list. Refer "Template Upload Portal - Overview" file.'), 
    ('Seedling Database', 'Tree Species', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Tree Species', 'Value Restriction Check', None, 'Tree Species', 'Tree Species', 'The value should be from the existing tree species list. Refer "Template Upload Portal - Overview" file.')
]
test_list_2 = [
    ('Seedling Database', 'BC Farmer', 'Data Type Check', 'Boolean', None, None, 'Entry has to be either "True" or "False".'), 
    ('Seedling Database', 'BC Farmer', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Certification', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Certification', 'Value Restriction Check', None, 'Certifications', 'Certification', 'The value should be from the existing certifications list. Refer "Template Upload Portal - Overview" file.'), 
    ('Seedling Database', 'Country', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Country', 'Value Restriction Check', None, 'Countries', 'Countries', 'The value should be from the existing Countries list. Refer "Template Upload Portal - Overview" file.'), 
    ('Seedling Database', 'Distribution Date', 'Data Type Check', 'Date', None, None, 'Entry has to be a date of format DD/MM/YYYY.'), 
    ('Seedling Database', 'Distribution Date', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Farmer Code', 'Master Data Check', None, 'ZFarmerSnap', 'FARMER_CODE', 'Farmer code has to be in line with farmer code in our sustainability database.'), 
    ('Seedling Database', 'Farmer Code', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Farmer Code;Distribution Date;Tree Species', 'Primary Key Check', None, None, None, 'Each row should contain a unique value. If the primary key is a combination of two or more columns, make sure the combination serves as a unique identifier.'), 
    ('Seedling Database', 'Number of Seedlings', 'Data Type Check', 'Integer', None, None, 'Entry has to be an integer {...-2, -1, 0, 1, 2,...}.'), 
    ('Seedling Database', 'Number of Seedlings', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'PES agroforestry program', 'Data Type Check', 'Boolean', None, None, 'Entry has to be either "True" or "False".'), 
    ('Seedling Database', 'PES agroforestry program', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Project', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Project', 'Value Restriction Check', None, 'Projects', 'Project', 'The value should be from the existing projects list. Refer "Template Upload Portal - Overview" file.'), 
    ('Seedling Database', 'Tree Species', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Seedling Database', 'Tree Species', 'Value Restriction Check', None, 'Tree Species', 'Tree Species', 'The value should be from the existing tree species list. Refer "Template Upload Portal - Overview" file.'),
    ('Seedling Database', 'BC Farmer', 'Data Type Check', 'Boolean', None, None, 'Entry has to be either "True" or "False".'), 
    ('Seedling Database', 'BC Farmer', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Deliveries Database', 'Certification', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Deliveries Database', 'Certification', 'Value Restriction Check', None, 'Certifications', 'Certification', 'The value should be from the existing certifications list. Refer "Template Upload Portal - Overview" file.'), 
    ('Deliveries Database', 'Country', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Deliveries Database', 'Country', 'Value Restriction Check', None, 'Countries', 'Countries', 'The value should be from the existing Countries list. Refer "Template Upload Portal - Overview" file.'), 
    ('Deliveries Database', 'Distribution Date', 'Data Type Check', 'Date', None, None, 'Entry has to be a date of format DD/MM/YYYY.'), 
    ('Deliveries Database', 'Distribution Date', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Deliveries Database', 'Farmer Code', 'Master Data Check', None, 'ZFarmerSnap', 'FARMER_CODE', 'Farmer code has to be in line with farmer code in our sustainability database.'), 
    ('Deliveries Database', 'Farmer Code', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Deliveries Database', 'Farmer Code;Distribution Date;Tree Species', 'Primary Key Check', None, None, None, 'Each row should contain a unique value. If the primary key is a combination of two or more columns, make sure the combination serves as a unique identifier.'), 
    ('Deliveries Database', 'Number of Seedlings', 'Data Type Check', 'Integer', None, None, 'Entry has to be an integer {...-2, -1, 0, 1, 2,...}.'), 
    ('Deliveries Database', 'Number of Seedlings', 'Missing Data Check', None, None, None, 'Entry should not be blank.'), 
    ('Deliveries Database', 'PES agroforestry program', 'Data Type Check', 'Boolean', None, None, 'Entry has to be either "True" or "False".'), 
    ('Deliveries Database', 'PES agroforestry program', 'Missing Data Check', None, None, None, 'Entry should not be blank.')
]


# for sheet_name, column_name, validation, validation_type, lookup_table, lookup_column, description in test_list:

mapping_df = pd.DataFrame(test_list, columns=["sheetname", "column_name", "validation", "validation_type", "lookup_table", "lookup_column", "description"])
# dk = df.groupby("validation")
# for name, group in dk:
#     print(f"group name {name} ")
#     print(group)
print(mapping_df)
# mapping_df["full_checks"] = mapping_df["validation"] +" "+ mapping_df["validation_type"].fillna('')

# change_index = mapping_df[mapping_df["sheetname"] != mapping_df["sheetname"]
# .iloc[0]].index [0]

# df1 = mapping_df.iloc[:change_index]
# df2 = mapping_df.iloc[change_index:]

# print(df1,df2)