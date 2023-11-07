import pandas as pd

df = pd.read_csv("imdb.csv")

# print(df)
# print(df.columns)
# print(df["Record"])

# 1
result = df
result = df.columns
result = df.info

# 2
result = df.head()

# 3
result = df.head(10)

# 4
result = df.tail()

# 5
result = df.tail(10)

# 6
result = df["Movie_Title"]

# 7
result = df["Movie_Title"].head()

# 8
result = df[["Movie_Title","Rating"]].head()

# 9
result = df[["Movie_Title","Rating"]].tail(7)

# 10
result = df[5:][["Movie_Title","Rating"]].head()

# 11
result = df[df["Rating"] >= 8.0][["Movie_Title","Rating"]].head(50)

# 12
result = df[(df['YR_Released'] >= 2014) & (df['YR_Released'] <= 2015)]["Movie_Title"]

# 13
result = df[(df['Num_Reviews'] > 10000) | ((df['Rating'] >= 8.0) & (df['Rating'] < 9.0))]



print(result)