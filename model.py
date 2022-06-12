import pandas as pd
import numpy as np

df =pd.read_csv("test.csv")
#df.dropna(subset=['Output'],inplace=True)
print (df.isnull().sum())

df['Output'].mask(df['Output'] ==1,'1', inplace=True)
df['Output'].mask(df['Output'] ==2 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==3 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==4 ,'1', inplace=True)
df['Output'].mask(df['Output'] ==5 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==6 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==7 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==8 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==9 ,'0', inplace=True)

df.dropna(subset=['Output','Glucose','retinopathy','BMI','Blood pressure'], inplace=True)
print(df)
print(df['Output'].value_counts())