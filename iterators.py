# iterator = yineleyici
# iterable = yinelenebilir

# Listeler ve tuplelar gibi for döngüsüyle yineleyebildiğimiz
# nesnelere iterable (yinelenebilir) nesne deriz.

# -------------- ÖRNEK 1 --------------

"""liste = [1,2,3,4,5]

iterator = iter(liste)     # __iter__() fonksiyonuyla listemizi iterable olarak tanımlıyoruz.
                           # for döngüleri bunu otomatik olarak yapar.
print(next(iterator))     
print(next(iterator))      # sonrasında __next__() fonksiyonuyla her seferinde sıradaki
print(next(iterator))      # indexi ekrana yazdırıyoruz.
print(next(iterator))
print(next(iterator))
# print(next(iterator))"""

# -------------- ÖRNEK 2 --------------

# AŞAĞIDAKİ DÖNGÜLER AYNI İŞİ GÖRÜR !!!

"""liste = [1,2,3,4,5]

for i in liste:            # for döngüsüyle işi otomatik yapıyoruz.
	print(i)

iterator = iter(liste)    # buradaysa listeyi iterable olarak tanımlıyoruz

while True:
	try:
		element = next(iterator)   # while döngüsüyle tek tek sıradaki ögeyi element'e tanımlayacağız
		print(element)             # her seferinde elementi yazdıracağız
	except StopIteration:          # ögelerin hepsi yazdırıldığında döngüyü break'leyeceğiz.
		break""" 

# -------------- ÖRNEK 3 --------------

# flag 1: Nesne için __iter__() fonksiyonunu etkinleştiriyoruz.
# bu sayede for döngüsü nesneyi iterable kabul edip sıralayabilecek.
# Eğer etmezsek şu hatayı alırız: "TypeError: 'MyNumbers' object is not iterable"

# flag 2: Nesne için __next__() fonksiyonunu etkinleştiriyoruz.
# bu sayede for döngüsü her seferinde sıradaki elemanı i
# değişkenimize atayacak ve print'le döndürecek.
# Eğer yapmazsak şu hatayı alırız: "TypeError: iter() returned non-iterator of type 'MyNumbers'"

class MyNumbers:                              # kendi liste sınıfımızı tanımladık !
	def __init__(self, start, stop):
		self.start = start                    # bir başlangıç ve
		self.stop = stop                      # bir bitiş sayısı tanımladık.

	def __iter__(self):          # flag 1
		return self

	def __next__(self):          # flag 2
		if self.start <= self.stop:           # ilk ve son sayı dahil olmak üzere aradaki
			x = self.start                    # tüm değerleri x değişkenine atadık.
			self.start += 1
			return x                          # son sayıya kadar hepsini x ile döndürdük.
		else:
			raise StopIteration               # tüm değerler döndükten sonra hata verdik.

list = MyNumbers(20,50)

"""for i in list:
	print(i)"""

myiter = iter(list)

"""print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))"""

while True:
	try:
		element = next(myiter)
		print(element)
	except StopIteration:
		break
