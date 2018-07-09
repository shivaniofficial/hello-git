import pandas as pd

#question = 1 :
d = {"Name" : pd.Series(['Shivani','Laddu','Kannu']),
     "Age" : pd.Series([19,23,20]),
     "Mail_id" : pd.Series(["shivani@123","laddu@456","kannu@789"]),
     "P_No." : pd.Series([123456789,456789123,789123456])}
df = pd.DataFrame(d)
print("Information is : ")
print(df)

#question = 2 :
df2 = pd.read_csv("weather.csv")
print(df2)
# to print the first 5 rows of DataFrame
print("first 5 rows of dataframe")
print(df2.head(5))
# to print first 10 rows of the DataFrame
print("first 10 rows of dataframe")
print(df2.head(10))
# basic statistics on DataFrame df
print("basic statistics")
print("\nTranspose")
print(df2.T)
print("\naxes")
print(df2.axes)
print("\ndatatypes")
print(df2.dtypes)
print("\nempty")
print(df2.empty)
print("\nndim")
print(df2.ndim)
print("\nshape")
print(df2.shape)
print("\nsize")
print(df2.size)
print("\nvalues")
print(df2.values)
# last 5 rows of data frame :
print("last 5 rows of dataframe")
print(df2.tail(5))
# extracting 2nd column :
print("extracting 2nd column of the DataFrame : ")
shiv = df2.T
newdf = (shiv[1:2]).T
print(newdf)
# basic operations on second column :
newdf = pd.DataFrame(newdf)
print("\naxes of 2nd column")
print(newdf.axes)
print("\nshape of 2nd column")
print(newdf.shape)