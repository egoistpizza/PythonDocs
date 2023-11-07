import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("li",{"class":"column"})

counter = 0

for laptop in list:
	deviceName = laptop.div.div.a.get("title")
	link = laptop.div.a.get("href")
	oldPrice = laptop.find("div",{"class":"proDetail"}).find("span",{"class":"oldPrice cPoint priceEventClick"}).find("del").text.strip().strip("TL")
	newPrice = laptop.find("div",{"class":"proDetail"}).find("span",{"class":"newPrice cPoint priceEventClick"}).ins.text.strip().strip("TL")
	counter += 1

	print(f"{str(counter).ljust(2)} - {deviceName}\n- Eski Fiyat: {oldPrice} - Yeni Fiyat: {newPrice}\n- Link: {link}\n")
