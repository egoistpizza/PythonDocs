# Bir x fonksiyonu tanımlıyoruz ve bu fonksiyondan
# içerisinde bulunan y isimli farklı bir fonksiyonu döndürmesini
# istiyoruz. Sonrasında x(parametre) tanımlı bir işlemi z'ye aktarıyoruz.

# Bu durumda z'yi çalıştırdığımızda x'in içerisindeki y döndürülecek.
# fakat biz x'e parametre vermiştik, hata alırız. z(parametre2)
# tanımladığımızda parametre2 y'nin parametresi yerine çalışır ve
# işlem sorunsuz şekilde tamamlanır.

# ------- ÖRNEKLER -------

"""def usalma(number):

	def inner(power):
		return number ** power

	return inner

two = usalma(2)       # flag
three = usalma(3)     # flag

print(two(3))         # flag
print(three(4))"""    # flag

"""def yetki_sorgula(page):

	def inner(role):
		if role == "Admin":
			return f"{role} rolünün {page} sayfasına ulaşabilir."
		else:
			return f"{role} rolü {page} sayfasına ulaşamaz."

	return inner

user = yetki_sorgula("Product Edit")   # flag
print(user("Admin"))                   # flag
print(user("User"))"""                 # flag

"""def islem(islem_adi):

	def toplama(*args):
		toplam = 0
		for i in args:
			toplam += i
		return toplam

	def carpma(*args):
		carpim = 1
		for i in args:
			carpim = carpim * i
		return carpim

	if islem_adi == "toplama":
		return toplama                # flag
	else:
		return carpma                 # flag

toplama = islem("toplama")            # flag
carpma = islem("carpma")              # flag

print(toplama(884,6,110))
print(carpma(10,10,10))"""
