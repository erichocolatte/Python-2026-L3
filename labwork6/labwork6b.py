import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/home/erica/Documents/USTH/Courses/Python Advanced/Python-2026-L3/labwork5/scores.csv')
df2 = df[:].dropna()

plt.scatter(df2.index, df2['math'],label='Math', color='red')
plt.scatter(df2.index, df2['python'], label='Python', color='blue')
plt.scatter(df2.index, df2['database'], label='DB', color='green')
plt.legend()
plt.savefig("scattered.png")
df3 = df2[["python", "math", "database"]].mean(axis=1)
df3[["python", "math", "database"]].hist(subplots=True, edgecolor="black")
plt.savefig("histo.png")
plt.show()


plt.savefig("box.png")