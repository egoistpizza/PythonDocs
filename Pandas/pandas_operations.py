import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,20,40,50],
    "Column3": ["abc","bcaa","ad","cba","dea"]
}

df = pd.DataFrame(data)

def kareAl(x):
    return x * x

kareAl2 = lambda x: x * x

result = df
result = df["Column2"].unique()   # Tekrarlayan alanlar elenir
result = df["Column2"].nunique()   # Farklı veri sayısını döndürür
result = df["Column2"].value_counts()   # Her veriden kaç tane olduğunu döndürür
result = df["Column1"] * 2
result = kareAl(df["Column1"])
result = df["Column1"].apply(kareAl)   # Parametredeki methodu DataFrame'e uygular, fonksiyon parametrelerini kendisi gönderir
result = df["Column1"].apply(kareAl2)
result = df["Column1"].apply(lambda x: x * x)
result = df["Column3"].apply(len)
df["Column4"] = df["Column3"].apply(len)

result = df
result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("Column2")
result = df.sort_values("Column3")
result = df.sort_values("Column2", ascending = False)
print(result)

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)
result = df

df = df.pivot_table(index = "Ay",columns = "Kategori",values = "Gelir")
result = df

# print(result)
