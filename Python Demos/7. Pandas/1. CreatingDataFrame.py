import pandas as pd 
# 1. Data Frame using list
lst = ['Ravi','Vikash']
df = pd.DataFrame(lst)
print(df)
# 2. Data frame using dictionary of ndarray/list
data = {'Name':['Ravi','Vikash'], 'Age':[23,20]}
df = pd.DataFrame(data)
print(df)
# 3. Data frame using reading an excel file
fileurl = r'E:\FL_insurance_sample.csv'
data = pd.read_csv(fileurl, index_col ="policyID")
df = pd.DataFrame(data)
print(df)