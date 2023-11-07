# Dokümantasyon: https://www.w3schools.com/python/python_json.asp

# JSON = JavaScript Object Notation
# Web tabanlı sistemlerde veri tabanı işlemleri için oldukça pratik bir
# dosya türüdür. Dictionary veri tipine çok benzer, dönüşümler yapabiliriz.

# dict
# key - value

import json   # modülümüzü içe aktarıyoruz

# print(dir(json))

personString = '{"name":"Ali","languages":["Python","Rust","JavaScript"]}'
# Görünüşte normal bir dictionary, tek fark tırnak işaretleri içerisine alınıp
# String olarak tanımlanması.

# ------- JSON'DAN DICT'E ÇEVİRMEK -------

# result = json.loads(personString)

# print(type(result))   # <class 'dict'>

# result = result["name"]
# result = result["languages"]

# ------- JSON DOSYASINDAN İŞLEM YAPMAK: -------

"""with open("person.json") as file:
	data = json.load(file)
	print(data)
	print(data["name"])
	print(data["languages"])"""

# ------- DICT'TEN JSON'A ÇEVİRMEK -------

person_dict = {
	"name": "Mehmet",
	"languages": ["C#","C++","C","CSS","HTML"]
}

# result = json.dumps(person_dict)

# print(type(result))   # <class 'str'>

# ------- JSON DOSYASI OLUŞTURMA -------

"""with open("person.json","w") as file:
	json.dump(person_dict, file)"""

# ------- JSON ÇIKTISINI ÖZELLEŞTİRME -------

personDict = json.loads(personString)

result = json.dumps(person_dict, indent = 4, sort_keys = True)

print(personDict)
print(result)