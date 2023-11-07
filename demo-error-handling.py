# Hata ve hata analizi konusundaki deneme notları.
liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

"""sayisalDegerler = []

for i in liste:
	try:
		j = int(i)
		sayisalDegerler.append(i)
	except ValueError:
		pass

print(sayisalDegerler)"""

# 2: Kullanıcı q değerini girmedikçe aldığınız her inputun
# sayı olduğundan emin olunuz aksi halde hata mesajı yazınız.

"""flag = True

while flag:
	deger = input()
	if deger == "q":
		flag = False
	else:
		try:
			sayisalKontrol = float(deger)
			pass
		except ValueError:
			print("Girilen değer sayı değil!")"""

# 3: Girilen parola içinde Türkçe karakter hatası veriniz.

"""import string

karakterler = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

parola = input("Parola giriniz: ")

for i in parola:
	if i in karakterler:
		pass
	else:
		raise TypeError("Ascii karakter kullanınız!")"""

# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajı veriniz.

"""import math

try:
	number = int(input("Sayı giriniz: "))
	print(math.factorial(number))
except ValueError:
	print("Lütfen yalnızca sayı giriniz:	")"""