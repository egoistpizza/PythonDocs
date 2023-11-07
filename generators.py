# GENERATORS Nedir?

# Generator, bellekte yer kaplamayan iteratorlara verilen addır.
# Bunlar anlık olarak oluşturulup tek sefer kullanılır.
# Bu sayede bellekte yer kaplamadan işlemleri hallederiz.

# -------------- ÖRNEK 1 --------------

# flag 1: her zaman yaptığımız gibi bir fonksiyon tanımladık. 0'dan 5'e kadar olan sayıların
# küplerini alıp çevirecek. Peki ya çok daha büyük bir aralıktaki sayıların küplerini almamız
# gerekse performans'ın içinden mi geçeceğiz? Tabi ki hayır!

# flag 2: yield keyword'unu kullanarak fonksiyonu bir GENERATOR haline getirdik. 50000 ve hatta
# daha yüksek aralıktaki sayıların rahatça küpünü alabiliriz, bu işlem tek bir kez yapılacak
# ve sonuç döndürülecek. Bellekte tutulmayacağı için PERFORMANS korunur.

# flag 3: for döngüsüyle cube() fonksiyonunu (bu bir generator) çalıştırdık ve 0-50000 aralığındaki
# tüm sayıların küpünü alıp ekrana yazdırdık. Rahat bir işlemdi, problem yaşanmadı.

"""def cube():                  # flag 1
	result = []

	for i in range(5):
		result.append(i**3)
	return result

print(cube())"""

"""import time                # sadece meraktan için ölçüm yaptım

start = time.time()

def cube():
	for i in range(500000):
		yield i ** 3"""        # flag 2

# generator = cube()

# iterator = iter(generator)

"""print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))"""

"""for i in cube():          # flag 3
	print(i)

finish = time.time()

result = str(finish - start)

print(f"\nİşlem {result} süre içerisinde sonlandı.")"""

# -------------- ÖRNEK 2 --------------

# flag 4: aşağıdaki kullanımda TUPLE otomatik olarak GENERATOR tanımlanır.

# flag 5: tuple'ı for döngüsüyle ekrana kolayca yazdırdık.

"""generator = (i**3 for i in range(5))           # flag 4
print(generator)"""

"""print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))"""

"""for i in generator:                 # flag 5
	print(i)"""
