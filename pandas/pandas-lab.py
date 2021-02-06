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

# cov() - Covariance indicates how two variables are related. A positive
# covariance means the variables are positively related, while a negative
# covariance means the variables are inversely related. Drawback of covariance
# is that it does not tell you the degree of positive or negative relation
# creating covariance on dataframe
df = pd.read_csv('iris.csv')
print(df.cov())

# corr() - correlation tells you the degree to which the
# variables tend to move together. You will always talk about
# correlation as a range between -1 and 1.
# creating correlation matrix on dataframe
df = pd.read_csv('iris.csv')
print(df.corr())

# merge / join
# concat or append operation
data = {
        'emp_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Jason', 'Andy', 'Allen', 'Alice', 'Amy'],
        'last_name': ['Larkin', 'Jacob', 'A', 'AA', 'Jackson']}
df_1 = pd.DataFrame(data, columns=['emp_id', 'first_name', 'last_name'])

data = {
        'emp_id': ['4', '5', '6', '7'],
        'first_name': ['Brian', 'Shize', 'Kim', 'Jose'],
        'last_name': ['Alexander', 'Suma', 'Mike', 'G']}
df_2 = pd.DataFrame(data, columns=['emp_id', 'first_name', 'last_name'])

# using concat
df = pd.concat([df_1, df_2])
print(df)

# using append
print(df_1.append(df_2))

# join the two dataframes along columns
print(pd.concat([df_1, df_2], axis=1))

# merge two dataframes based on the emp_id value
# in this case only the emp_id's present in both table will be joined
print(pd.merge(df_1, df_2, on='emp_id'))

# left join
print(pd.merge(df_1, df_2, on='emp_id', how='left'))

# merge while adding a suffix to duplicate column names of both table
print(pd.merge(df_1, df_2, on='emp_id', how='left', suffixes=('_left', '_right')))

# right join
print(pd.merge(df_1, df_2, on='emp_id', how='right'))

# inner join
print(pd.merge(df_1, df_2, on='emp_id', how='inner'))

# outer join two frames
print(pd.merge(df_1, df_2, on='emp_id', how='outer'))

# pg98 grouping
