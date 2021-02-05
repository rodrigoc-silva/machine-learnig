# pandas
# creating a pandas series
# creating a series by passing a list of values, and a custom index label.
import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3, np.nan, 5, 6], index=['A', 'B', 'C', 'D', 'E', 'F'])
print(s)

# creating a pandas dataframe
data = {'Gender':['F', 'M', 'M'], 'Emp_ID': ['E01', 'E02', 'E03'],
        'Age': [25, 27, 25]}
# we want the order the columns, so lets specify in columns parameter
df = pd.DataFrame(data, columns=['Emp_ID', 'Gender', 'Age'])
print(df)

# reading / writing data from csv, text, Excel
# df = pd.read_csv('mtcars.csv')
# df = pd.read_csv('mtcars.txt', sep='\t')
# df = pd.read_excel('mtcars.xlsx')
# reading for multiple sheets of same Excel into different dataframes
# xlsx = pd.ExcelFile('mtcars.xlsx')
# sheet1_df = pd.read_excel(xlsx, 'Sheet1')
# sheet2_df = pd.read_excel(xlsx, 'Sheet2')

# writing
# index = False parameter will not write the index values, default is True
# df.to_csv('newFile.csv', index=False)
# df.to_csv('newFile.txt', sep='\t', index=False)
# df.to_excel('newFile.xlsx', sheet_name='1', index=False)

# basic statistics on dataframe
# describe() returns min, first quartile, median,
# third quartile, max on each column
df = pd.read_csv('iris.csv')
print(df.describe())
