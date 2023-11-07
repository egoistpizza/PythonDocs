# requests module
import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
# result = result.text  # konsola yazdırır.
result = json.loads(result.text)

print(result) # response[200] = başarılı
print(result[0])
print(result[0]["title"])

for i in result:
	if i["userId"] == 1:
		print(i)
		print(i["title"])
	print(i)
	print(i["title"])

print(type(result))
