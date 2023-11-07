# Daha fazla bilgi için <https://www.w3schools.com/python/python_ref_list.asp> adresine gidiniz.

numbers = [65,35,18,6,74]
letters = ['l','p','e','x','w']

# minimum = min(numbers)
# maximum = max(numbers)
# minimum = min(letters)
# maximum = max(letters)

# index = numbers[3:]
# index = letters[:3]

# numbers[2] = 48
# letters[3:] = ['y','z']

# length = len(numbers)
# length = len(letters)

# -----------------------------  Metotlar  -----------------------------

# .append() metodu, listenin sonuna veri eklememizi sağlar. Direkt olarak listeyi günceller.
# numbers.append(684)
# letters.append('g')

# .insert() metodu, listenin istediğimiz index'ine veri eklememizi sağlar. 1. parametre olarak index, 2. parametre olarak da eklemek istediğimiz veriyi gireriz. Direkt olarak listeyi günceller.
# numbers.insert(2,17)
# letters.insert(0,'z')

# .pop() metodu, istediğimiz index'deki veriyi silmemizi sağlar. Silmek istediğimiz veriye ait index'i parametre olarak veririz. Direkt olarak listeyi günceller.
# numbers.pop(3)
# letters.pop(1)

# .remove() metodu, istediğimiz veriyi silmemizi sağlar. Parametre olarak silmek istediğimiz veriyi veririz. Direkt olarak listeyi günceller.
# numbers.remove(35)
# letters.remove('x')

# .sort() metodu, verileri sayısal veya alfabetik olarak sıralamamızı sağlar. Direkt olarak listeyi günceller.
# numbers.sort()
# letters.sort()

# .reverse metodu, verileri tersten sıralamamızı sağlar. .sort() metodunun ardından kullanılması durumunda verileri sayısal veya alfabetik olarak tersten sıralama imkanı sunar. Direkt olarak listeyi günceller.
# numbers.reverse()
# letters.reverse()

# .clear() metodu, listedeki tüm verileri silmemizi sağlar. Direkt olarak listeyi günceller.
# numbers.clear()
# letters.clear()

# .count() metodu, string ifadelerde olduğu gibi, listedeki istediğimiz verinin kaç defa bulunduğunu verir. Parametre olarak saymak istediğimiz veriyi veririz.
# print(numbers.count(6))
# print(letters.count('w'))

# Not: Eğer listenin en son index'ine veri eklemek istersek .insert(len(LİST),'VERİ') yolunu izleriz.

print()