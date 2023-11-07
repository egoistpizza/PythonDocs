"""with open("newfile.txt","r+",encoding="utf-8") as file:
	file.seek(10)
	file.write("C") 

with open("newfile.txt","r+",encoding="utf-8") as file:
	print(file.read()) """

# ********** Sayfa sonunda güncelleme *************

"""with open("newfile.txt","a",encoding="utf-8") as file:
	file.write("\nULU ÖNDER MUSTAFA KEMAL ATATÜRK")
with open("newfile.txt","r",encoding="utf-8") as file:
	print(file.read())"""

# ********** Sayfa başında güncelleme ***********

"""with open("newfile.txt","r+",encoding="utf-8") as file:
	content = file.read()
	content = "ATATÜRK'ÜN GENÇLİĞE HİTABESİ\n\n" + content
	file.seek(0)
	file.write(content)

with open("newfile.txt","r",encoding="utf-8") as file:
	print(file.read())"""

# *********** Sayfa ortasında güncelleme ************

"""with open("newfile.txt","r+",encoding="utf-8") as file:
	list = file.readlines()
	list.insert(2,"Ey Türk gençliği! Birinci vazifen; Türk istiklalini, Türk cumhuriyetini, ilelebet muhafaza ve müdafaa etmektir.\n\n")
	file.seek(0)
	file.writelines(list)
	print(file.read())
"""

# file.writeline() methodu bir listeyi yazdırır.