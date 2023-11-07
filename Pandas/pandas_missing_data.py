import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index=["a","c","e","f","h"], columns=["column1","column2","column3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

result = df
result = df.drop("column1", axis= 1)
result = df.drop(["column1","column2"], axis= 1)
result = df.drop("a", axis= 0)
result = df.drop(["a","b","h"], axis= 0)

result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df["column1"].isnull().sum()

# result = df

result = df["column1"].isnull()
result = df[df["column1"].isnull()]
result = df[df["column1"].notnull()]
result = df[df["column1"].isnull()]["column1"]
result = df[df["column1"].notnull()]["column1"]

result = df.dropna()   # default olarak axis = 0 -> satırda işlem yapar
result = df.dropna(axis = 1)   # axis = 1 -> sütunda işlem yapar
result = df.dropna(how = "any")  # default -> how = "any"
result = df.dropna(how = "all")
result = df.dropna(subset = ["column1","column2"])
result = df.dropna(subset = ["column1","column2"], how = "all")
result = df.dropna(thresh = 2)  # x normal değer varsa silmez
result = df.dropna(thresh = 4)  # 4 normal veri varsa silmez
result = df.dropna(thresh = 3)  # 3 normal veri varsa silmez

result = df.fillna("boş")
result = df.fillna(value= "no input")
result = df.fillna(value= 1)

def fillMean(df):
    """Fills the NaN spaces in the DataFrame with the average of that column.

    Args:
        df (pandas.DataFrame, necessary): DataFrame to be patched.
    """
    patchedDF = df
    for column in df.columns:
        mean = df[column].mean()
        patchedDF[column] = df[column].fillna(mean)
    return patchedDF

patchedDF = fillMean(df)

print(patchedDF)
print(result)