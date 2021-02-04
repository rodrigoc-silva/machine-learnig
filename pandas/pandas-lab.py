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

# page 90 reading and writing data
