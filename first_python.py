%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')
df_can.head()
# columns and indexing
df_can.columns
df_can.index

# the default indexing and column are not in a list form

# so we need to convert them into a list
print(type(df_can.columns))
print(type(df_can.index))
df_can.columns.to_list()
df_can.index.to_list()

# after we changedin to a list lets look at their type

print(type(df_can.columns))
print(type(df_can.index))
