import numpy as np
import pandas as pd

df = pd.read_csv('/home/erica/Documents/USTH/Courses/Python Advanced/Python-2026-L3/labwork5/students.csv')
d = pd.read_csv('/home/erica/Documents/USTH/Courses/Python Advanced/Python-2026-L3/labwork5/scores.csv')

print(df.head())
print(df.shape)
print(df[['name', 'GPA']])
print(df[df['GPA'] >= 3.5])
print(df.sort_values('GPA'))
print(df.groupby('major')['GPA'].mean())

print(d.isna().sum())
print(df.isna().sum())
df2 = df[:].dropna()
d2 = d[:].dropna()
dmerged = pd.merge(df2, d2, on='student_id')
print(dmerged)

dmerged["average"] = dmerged[["python", "math", "database"]].mean(axis=1)
print(dmerged['average'])

print(dmerged.sort_values('average', ascending=False).head())
avg_score = dmerged.groupby('major')['average'].mean()
print(avg_score)