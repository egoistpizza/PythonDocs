import pandas as pd

df = pd.read_csv("nba.csv")

# 1- İlk 10 kaydı getiriniz.
# print(df.head(10))

# 2- Toplam kaç kayıt vardır ?
# print(df.info)
# print(len(df.index))

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
# print(df["Salary"].mean())

# 4- En yüksek maaşı ne kadardır ?
# print(df["Salary"].max())

# 5- En yüksek maaşı alan oyuncu kimdir ?
# print(df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0])

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
# print(df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name","Team","Age"]].sort_values("Age",ascending = False))

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
# print(df[df["Name"] == "John Holland"]["Team"])

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
# print(df.groupby("Team")["Salary"].mean())

# 9- Kaç farklı takım mevcut ?
# print(len(df.groupby("Team")))
# print(df["Team"].nunique())

# 10- Her takımda kaç oyuncu oynamaktadır ?
# print(df["Team"].value_counts())

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
# df.dropna(inplace=True)
# print(df[df["Name"].str.contains("and")])

# def findAnd(name):
#     if "and" in name.lower():
#         return True
#     return False

# print(df[df["Name"].apply(findAnd)])
