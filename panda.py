#1,2....read csv file......
import pandas as pd
data=pd.read_csv(r"C:\Users\priya\OneDrive\Desktop\python\dataset\Ball_by_Ball.csv")

print(data)
print(data.head(20))

# 3....clean empty cell#
print("drop values")
print(data.dropna())

#remove duplicates#
print("duplicacy removal:-")
print(data.drop_duplicates())