import pandas as pd

customers = {
    "CustomerID": [1,2,3,4],
    "FirstName": ["Ahmet","Ali","Hasan","Canan"],
    "LastName": ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

orders = {
    "OrderID": [10,11,12,13],
    "CustomerID": [1,2,5,7],
    "OrderDate": ["2010-07-04","2010-07-04","2010-07-04","2010-07-04"]
}

df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)

# # Inner Join: Sipariş vermiş müşteriler ve siparişleri
# result = pd.merge(df_customers,df_orders,how="inner")

# # Left Join: Tüm müşteriler ve (varsa) siparişleri
# result = pd.merge(df_customers,df_orders,how="left")

# # Right Join: Tüm siparişler ve (varsa) siparişi veren müşteriler
# result = pd.merge(df_customers,df_orders,how="right")

# (Full) Outer Join: Tüm kayıtlar eklenir
result = pd.merge(df_customers,df_orders,how="outer")



customersA = {
    "CustomerID": [1,2,3,4],
    "FirstName": ["Ahmet","Ali","Hasan","Canan"],
    "LastName": ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    "CustomerID": [4,5,6,7],
    "FirstName": ["Yağmur","Çınar","Cengiz","Can"],
    "LastName": ["Bilgi","Turan","Yılmaz","Turan"]
}

df_customersA = pd.DataFrame(customersA)
df_customersB = pd.DataFrame(customersB)

# Merge

# result = pd.concat([df_customersA,df_customersB]) # defaut axis = 0, DataFrame'ler alt alta eklenir.
# result = pd.concat([df_customersA,df_customersB],axis=1) # axis = 1, DataFrame'ler yan yana eklenir.

print(result)