# Bu derste dosya içeriğini okumayı öğreneceğiz.

# READING zaten varsayılan mod olduğu için open() fonksiyonuna
# 2. bir parametre vermemiz gerekmiyor.

"""file = open("newfile.txt")
print(file)"""

# Eğer dosya belirtilen konumda yoksa EXCEPTION yersin:

"""Traceback (most recent call last):
  File "/home/egoist/Belgeler/PythonDocs/reading-files.py", line 6, in <module>
    file = open("newfile3.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'newfile3.txt'"""

# Bunu engellemek için:

"""try:
	file = open("newfile.txt")
	print(file)
except (FileNotFoundError, NameError):
	print("Kardeşim newfile var newfile2 var ne bakıyon?")
finally:
	file.close()
	print("Dükkan kapandı.")"""

# --------------------------------------- #

file = open("newfile.txt","r",encoding="utf-8")

# FOR DÖNGÜSÜYLE OKUMA :

# Satır satır veri döndürür. Arada boş satırlar verir.

"""for i in file:
	print(i)"""

# Satır satır veri döndürür. Arada boş satır BIRAKMAZ:

"""for i in file:
	print(i, end="")

file.close()"""

# .READ() METHODUYLA OKUMA :

"""content = file.read()
print(content)"""

# .read() methodunda CURSOR mantığı vardır. .read() methoduyla
# bir dosyayı okuduğunuzda CURSOR DOSYANIN SONUNA GELİR ve eğer
# tekrar okutmak isterseniz buradan devam eder. Örneğin:

"""content1 = file.read()

print(content1)
print("İçerik 1 başarıyla ekrana yazdırıldı.")

content2 = file.read()

print(content2)
print("İçerik 2 başarıyla ekrana yazdırıldı.")"""

"""Çıktı:
Bu dosya çok önemli bilgiler içeriyor. Hem de çok önemli
Ama okumaman lazım dostum. 
İçerik 1 başarıyla ekrana yazdırıldı.

İçerik 2 başarıyla ekrana yazdırıldı."""

# Gördüğün gibi, cursor sonda kaldığı için içerik 2'de yazılacak
# bir şey kalmadı.

# Eğer içerik 2'den önce dosyayı tekrardan açsaydık sorun çözülürdü:

"""content1 = file.read()

print(content1)
print("İçerik 1 başarıyla ekrana yazdırıldı.")

file = open("newfile.txt","r",encoding="utf-8")   # flag

content2 = file.read()

print(content2)
print("İçerik 2 başarıyla ekrana yazdırıldı.")"""

"""Çıktı:
Bu dosya çok önemli bilgiler içeriyor. Hem de çok önemli
Ama okumaman lazım dostum. 
İçerik 1 başarıyla ekrana yazdırıldı.
Bu dosya çok önemli bilgiler içeriyor. Hem de çok önemli
Ama okumaman lazım dostum. 
İçerik 2 başarıyla ekrana yazdırıldı."""

# !!! CURSOR mantığı çok önemli.
# .read(size) methodu SIZE parametresi alır. Bu parametre okunacak BYTE (KARAKTER) sayısını verir.
# Üst üste kullanıldığında CURSOR kaldığı yerden okumaya devam eder.

"""content = file.read(5)
content = file.read(8)
content = file.read(3)
print(content)"""

# .READLINE() METHODU :
# Her seferinde 1 satır okur.
# Aralara boşluk bırakır.

"""content = file.readline()
print(content)
content = file.readline()
print(content)"""

# Boşluğu silmek için yine end="" parametresi verebiliriz.

"""content = file.readline()
print(content,end="")       # flag
content = file.readline()
print(content)"""

# .READLINES() METHODU:
# Her satırı listenin bir ögesi olarak kabul eder.

"""liste = file.readlines()
print(liste)"""

# Böylece her satıra index numarasıyla ulaşabiliriz.

"""liste = file.readlines()
print(liste[0])           # flag
print(liste[1])           # flag"""

file.close()