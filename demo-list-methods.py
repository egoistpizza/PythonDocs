names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1- 'Cenk' ismini listenin sonuna ekleyin.
'''names.append('Cenk')
print(names)'''

# 2- 'Sena' değerini listenin başına ekleyin.
'''names.insert(0,'Sena')
print(names)'''

# 3- 'Deniz' ismini listeden silin.
'''names.remove('Deniz')
print(names)'''
# veya
'''names.pop(3)
print(names)'''

# 4- 'Deniz' verisinin index'i nedir?
'''print(names.index('Deniz'))'''

# 5- 'Ali' listenin bir elemanı mıdır?
'''if names.count('Ali') > -1:
    print(True)
else:
    print(False)'''

# 6- Liste elemanlarını ters çevirin.
'''names.reverse()
print(names)'''

# 7- Liste elemanlarını alfabetik olarak sıralayın.
'''names.sort()
print(names)'''

# 8- years listesini rakamsal büyüklüğe göre sıralayın.
'''years.sort()
print(years)'''

# 9- str = 'Chevrole,Dacia' karakter dizisini listeye çevirin.
'''list1 = 'Chevrole,Dacia'.split(',')
print(list1)'''

# 10- years dizisinin en büyük ve en küçük elemanı nedir?
'''print(min(years))
print(max(years))'''

# 11- years dizisinde kaç tane 1998 değeri vardır?
'''print(years.count(1998))'''

# 12- years dizisinin tüm elemanlarını silin.
'''years.clear()
print(years)'''

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayın.
'''input0 = input('Marka Giriniz : ')
input1 = input('Marka Giriniz : ')
input2 = input('Marka Giriniz : ')
list1 = [input0,input1,input2]
print(list1)'''

# veya

'''sayac = 0
list1 = ''
while sayac < 3:
    if sayac < 2:
        string = input('Marka Giriniz : ')
        list1 += string + '-'
        sayac += 1
    else:
        string = input('Marka Giriniz : ')
        list1 += string
        sayac += 1
print(list1.split('-'))'''

# veya (Alttaki birincil tercihtir.)

'''sayac = 0
list1 = []
while sayac < 3:
    string = input('Marka Giriniz : ')
    list1.append(string)
    sayac += 1
print(list1)'''