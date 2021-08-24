import pandas as pd
fileurl = r'E:\Coding\Python\Python-Practice\PythonDemos\7.Pandas\Resource\FL_insurance_sample.csv'
data = pd.read_csv(fileurl)
df = pd.DataFrame(data)
""" 1. Accessing Columns"""
# print(df[['policyID','statecode']])
"""2. Accessing first 5 rows"""
# first5Row = df.head(5)
# last5Row=df.tail(5)
# print(first5Row)
"""3. Accessing rows and columns by index"""
# policyData = df["policyID"] #read by column
# print(policyData)
# firstPlicyRow=df.loc[0] #read single row
# print(firstPlicyRow)
# print(df.loc[0:5]) # read first 5 row
# print(df.loc[0:5,['construction','policyID']]) # read first 5 row with selected column
# print(df.loc[[0,5],['construction','policyID']]) # read first and 5th row with selected column
"""4.  Operations"""
# print(df.loc[df['construction']=='Wood',['construction','policyID']].head(5)) #read first 5 row where construction=Wood

# print(df['policyID'].groupby(df['construction']).count())

"""5. Missing Data"""

# print(df.isnull().sum()) #find all columns sum with null value
df.fillna(df['point_latitude'].median(), inplace=True) #Replace missing value of specific column with median val of that column
# df.fillna('NA',inplace=True)
print(df.isnull().sum())