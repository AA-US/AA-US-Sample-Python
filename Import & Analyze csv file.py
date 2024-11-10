# Process of analyzing your data.
# Import python libraries required.
import pandas as pd
import matplotlib as plt

# reading data from a csv file and assigning it to a data frame
sales = pd.read_csv(‘C:/Desktop/2018-2019 Data.csv')

# Understanding  your data. Getting info on column names,
# data type, null or not null & count of rows. 
# Plus basic descriptive statistics Sales.min()

sales.Info()

Sales.max()

sales.mean(numeric_only = True)

sales['SalesAmount'].std()

sales.shape # count of rows & columns in dataframe

sales.describe()

sales.describe(include='object')
