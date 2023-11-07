# map(x,y) metodu, y değerindeki listede bulunan tüm değerlere x işlemini uygular.
# Varsayılan kullanımda print(map(x,y)) şeklinde ekrana yazdırılırsa döndürülecek sonucun
# bellek üzerindeki referans değerini ekrana yazdırır (örn. 1.1). Eğer döndürülmesi gereken sonucu
# ekrana yazdırmak istiyorsak ya list veri tipine çevirmeli (örn. 1.2) ya da
# ya da da for döngüsüne (örn. 1.3) almalıyız.

'''def square(value): return value ** 2

numbers = [1,2,3,4,5,6,7,8,9]
print(map(square,numbers)) # örn. 1.1
print(list(map(square,numbers))) # örn. 1.2
for item in numbers:
    print(square(item)) # örn 1.3'''

# lambda expression ise map() metodu kullanımında bir fonksiyon yerine anonymous bir işlem uygulamaya
# olanak tanır. (örn. 2.1)

'''numbers = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda value: value ** 2,numbers)))''' # örn. 2.1

# lambda expressions bir değişkene atanarak fonksiyon gibi kullanılabilir. (örn. 2.2)

'''square = lambda value: value ** 2

numbers = [1,2,3,4,5,6,7,8,9]
print((list(map(square,numbers))))''' # örn. 2.2

# filter() fonksiyonu, map() ile aynı işlemi yaparak verilen sonuçlar arasından sadece True
# döndürenlere ulaşabilmemizi sağlar. (örn. 3.1 veya örn. 3.2)

'''def checkEven(int): return int % 2 == 0 # Parametrenin 2'ye bölünme durumunu bool veri tipinde yansıtır.
numbers = [1,2,3,4,5,6,7,8,9]
evens = list(filter(checkEven,numbers))
print(evens)''' # örn. 3.1 (def)

'''checkEven = lambda int: int % 2 == 0 # Parametrenin 2'ye bölünme durumunu bool veri tipinde yansıtır.
numbers = [1,2,3,4,5,6,7,8,9]
evens = list(filter(checkEven,numbers))
print(evens)''' # örn. 3.2 (lambda)