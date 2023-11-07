# Value Types => str, int, float ### Senkronizasyon yok ! Farklı birimlerde depolanır !

x = 25
y = 10

x = y

y = 5

print(x,y)

# Referance Types => list ### Senkronizasyon var ! Aynı adreste depolanır !

a = ['Mango','Coconut']
b = ['Mango','Coconut']

a = b

b[1] = 'Orange'

print(a,b)