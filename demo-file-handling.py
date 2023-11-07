# Öğrenci kayıt uygulaması.

# Öncelikle sisteme hoca girer, 3 öğrencimize ait sınav notlarını girer. Sonrasında öğrenci sisteme giriş yapar ve ortalamasını öğrenir. Kendi ortalamasına ait
# harf karşılığını ve öğretmen notunu içeren bir txt dosyası elde eder.

passwd = {
	"root": 3546195116521656,
	"Mete Orhun": 9846,
	"Zeynep Çınar": 3546,
	"Eren Okur": 2168
}

def start():
	print("""
		- O -
		ÖĞRENCİ KAYIT PROGRAMINA HOŞ GELDİNİZ!
		1- ROOT GİRİŞİ
		2- ÖĞRENCİ GİRİŞİ
		q- ÇIKIŞ
		- O -
		""")
	option = input()
	if option == "1":
		rootGirisi()
	elif option == "2":
		ogrenciGirisi()
	elif option == "q":
		print("Başarıyla çıkış yaptınız!")
		raise SystemExit
	else:
		print("Hatalı seçenek tuşladınız!")
		raise SystemExit

def rootGirisi():
	password = int(input("Şifre giriniz: "))
	if password == passwd["root"]:
		with open("ogrenci-verileri.txt","w",encoding="utf-8") as data:
			data.write("Matematik Sınav Sonuçları:\n\n")
			while True:
				ogrenciAdi = input("Notları girilecek öğrenci adını giriniz: ")
				if ogrenciAdi == "q":
					break
					ogrenciGirisi()
				notlar = input("Notları aralarında virgülle giriniz: ")
				notlarList = notlar.split(",")
				data.write(f"{ogrenciAdi}: ,{notlarList[0]},{notlarList[1]},{notlarList[2]},\n")

	else:
		print("Hatalı şifre girdiniz!")
		raise SystemExit

def ogrenciGirisi():
	while True:
		name = input("İsim giriniz: ")
		password = int(input("Şifre giriniz: "))

		if passwd[name] == password:
			print("Başarılı bir şekilde sisteme giriş yaptınız!")
			with open("ogrenci-verileri.txt","r",encoding="utf-8") as file:
				list = file.readlines()
				if name == "Mete Orhun":
					ogrenciData = list[2]
					notlar = ogrenciData.split(",")
					print(f"\nSINAV SONUÇLARINIZ = 1. SINAV: {notlar[1]}, 2. SINAV: {notlar[2]}, 3. SINAV: {notlar[3]}.")
					with open(f"{name}.txt","w",encoding="utf-8") as results:
						results.write(f"\nSINAV SONUÇLARINIZ = 1. SINAV: {notlar[1]}, 2. SINAV: {notlar[2]}, 3. SINAV: {notlar[3]}.")
						print("Dosya dizininizde sonuçlarınız kaydedildi.")
				if name == "Zeynep Çınar":
					ogrenciData = list[3]
					notlar = ogrenciData.split(",")
					print(f"\nSINAV SONUÇLARINIZ = 1. SINAV: {notlar[1]}, 2. SINAV: {notlar[2]}, 3. SINAV: {notlar[3]}.")
					with open(f"{name}.txt","w",encoding="utf-8") as results:
						results.write(f"\nSINAV SONUÇLARINIZ = 1. SINAV: {notlar[1]}, 2. SINAV: {notlar[2]}, 3. SINAV: {notlar[3]}.")
						print("Dosya dizininizde sonuçlarınız kaydedildi.")
				if name == "Eren Okur":
					ogrenciData = list[4]
					notlar = ogrenciData.split(",")
					print(f"\nSINAV SONUÇLARINIZ = 1. SINAV: {notlar[1]}, 2. SINAV: {notlar[2]}, 3. SINAV: {notlar[3]}.")
					with open(f"{name}.txt","w",encoding="utf-8") as results:
						results.write(f"\nSINAV SONUÇLARINIZ = 1. SINAV: {notlar[1]}, 2. SINAV: {notlar[2]}, 3. SINAV: {notlar[3]}.")
						print("Dosya dizininizde sonuçlarınız kaydedildi.")
		else:
			print("Hatalı giriş denemesi!")
			break

start()