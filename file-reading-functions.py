# Biz normalde dosyalarımızı aşağıdaki şekilde açıp kapıyorduk.
# Fakat elbette daha kolay bir yöntemi var!

"""file = open("newfile.txt","r",encoding="utf-8")

content = file.read()
print(content)

file.close()
"""

# WITH komutu bir blok oluşturur. Bu bloğa dosyada yapılacak işlemleri yazarız
# ve blok sonunda dosya otomatik olarak kapanır. İstersek dosya açma fonksiyonumuzu
# AS aracılığıyla FILE gibi farklı bir değişkene kaydedebiliriz.

# file.read() fonksiyonuna göndereceğimiz parametre hangi byte'dan başlayarak
# okuyacağını belirler. flag 1

# file.seek() fonksiyonu imleci istediğimiz byte'a getirmemizi sağlar.
# parametre olarak byte'ı veririz. flag 2

# file.tell() fonksiyonu imlecin anlık olarak hangi byteda olduğunu döndürür. flag 3

"""with open("newfile.txt","r",encoding="utf-8") as file:
	content = file.read(10)   #  flag 1
	print(content)
	file.seek(0)              # flag 2
	print(file.tell())        # flag 3
	content2 = file.read()
	print(content2)"""

	# Daha fazla bilgi için https://www.w3schools.com/python/python_ref_file.asp