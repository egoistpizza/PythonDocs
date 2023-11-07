import pandas as pd

data = pd.read_csv("nba.csv").dropna()

data.dropna(inplace = True)

result = data.columns

# data["Name"] = data["Name"].str.upper()   # str method
# data["Name"] = data["Name"].str.lower() 
# result = (data["Name"].head())

# data["index"] = data["Name"].str.find("a")

# data = data.Name.str.contains("Jordan")
# data = data[data.Name.str.contains("Jordan")]
# data = data.Team.str.replace("Boston Celtics","Adana Demir Spor")

### ***
data[["FirstName","LastName"]] = data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True)
# Not: .loc methoduyla bölündüğünde 2 nesne elde edilen Name nesneleri True değeri döndürür ve bu nesneler bölünerek FirstName-LasstName kolonlarına aktarılır.


print(data.head())
# print(result)