# Bu derste dosya açma ve okumayı öğreneceğiz.

# Herhangi bir konumda dosya açmak için open(dosya_adi, erişim_modu) fonksiyonunu kullanıyoruz.
# erişim_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w" => Write, yazma modu. Dosyayı mevcut konumda oluşturur.
# "a" => Append, ekleme modu. Dosya konumda YOKSA oluşturulur.
# "x" => Create, oluşturma modu. Dosya zaten varsa HATA VERİR.
# "r" => Read, okuma modu. VARSAYILAN moddur. Dosya yoksa HATA VERİR.

# WRITE modunda dosyanın üstüne yazarsın, APPEND modundaysa ekleme yaparsın. Fark budur.
# .close() metodu dosyayı kapar, BELLEKTEN TASARRUF EDER.

# MEVCUT DİZİNDE DOSYA AÇMA:

"""file = open("newfile.txt","w")
file.close()"""

# FARKLI BİR DİZİNDE DOSYA AÇMA:

"""file = open("/home/egoist/Downloads/newfile.txt","w")
print(file)"""

# !!! Dosyaya bir şeyler yazmak için .write() metodunu kullanıyoruz.

"""file = open("newfile.txt","w")
file.write("Bu bir deneme dosyasidir.")
file.close()"""

# .open() metoduna 3. parametre olarak encoding="utf-8" verebiliriz.

"""file = open("newfile.txt","w",encoding="utf-8")
file.write("UTF-8 sayesinde tÜrkÇe karakterleri kullanabİlİrsİn!")
file.close()
"""

# APPEND modu ekleme yaptığı için, her çalıştırdığında metin tekrardan sona eklenecektir.

"""file = open("newfile.txt","a",encoding="utf-8")
file.write("Append modu da güzelmiş.")
file.close()"""

# X modu yalnızca dosya oluşturmak için kullanılır.

"""file = open("newfile2.txt","x",encoding="utf-8")"""

# X modunda dosya ZATEN BULUNUYORSA aşağıdaki hatayı verir:

"""Traceback (most recent call last):
  File "/home/egoist/Belgeler/PythonDocs/file-management.py", line 45, in <module>
    file = open("newfile2.txt","x",encoding="utf-8")
FileExistsError: [Errno 17] File exists: 'newfile2.txt'"""
