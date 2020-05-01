import pandas as pd
fileurl = r'E:\FL_insurance_sample.csv'
data = pd.read_csv(fileurl)
df = pd.DataFrame(data)
# 1. Accessing Columns
# print(df[['policyID','statecode']])
#2. Accessing first 5 rows
# first5Row = data.head(5)
# print(first5Row)
#3. Accessing rows and columns by index

