# Dokümantasyon: https://beautiful-soup-4.readthedocs.io/en/latest/#

# BeautifulSoup Nedir?
# BeautifulSoup, Web Scraping işlemlerinde kullandığımız
# bir kütüphanedir. HTML veya XML verisini parçalayarak analiz
# eder ve bu sayede istediğimiz bölümlere kolayca ulaşabilmemizi
# sağlar.

from bs4 import BeautifulSoup   # Kütüphanemizi içe aktarıyoruz

markup = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>HTML Document</title>
</head>
<body>


	<h1 id="header">
		Python BeatifulSoup için HTML öğrenmece!
	</h1>

	<div class="frameworkler">
		<h2>
			Framework'ler
		</h2>

		<ul>
<li>Django</li>
	<li>Numpy</li>
		<li>Pandas</li>
		</ul>
	</div>

	<div class="moduller">
<h2>
		Modüller
</h2>

	<ul>
		<li>Math</li>
		<li>Datetime</li>
		<li>Json</li>
		<li>Os</li>
		<li>Random</li>
		<li>Re</li>
		<li>Requests</li>
	</ul>
</div>

<img src="/home/egoist/Resimler/EgoistWallpapers/astronaut01.jpg">
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
	</body>
	</html>
"""   # (PARSE) Parçalanması ve analiz edilmesi için bir html kodu tanımladık

soup = BeautifulSoup(markup,"html.parser")    # Bu kodu BeautifulSoup'a göndererek analiz edilmesini sağlıyoruz.

result = soup.prettify()   # Kod düzenli bir şekilde (boşluklara dikkat edilerek) döndürülür.
result = soup.title   # Kod başlığı (ilk) döndürülür
result = soup.head   # Head bölümü (ilk) döndürülür
result = soup.body   # Body bölümü (ilk) dindürülür

result = soup.title.name   # Etiketin ismi döndürülür
result = soup.title.string   # Etiket içeriği döndürülür

result = soup.h1   # h1 etiketi döndürülür
result = soup.h2   # h2 etiketi döndürülür
result = soup.h2.name   # h2 etiketinin ismi (h2 işte) döndürülür
result = soup.h2.string   # h2 etiketinin içeriği döndürülür
result = soup.h1.string   # h1 etiketinin içeriği döndürülür

result = soup.find_all("h2")   # find_all() metodu bir liste döndürür!
result = soup.find_all("h2")[0]   # bu sayede indexleyerek işlem yapabiliriz
result = soup.find_all("h2")[1]   # ya da for döngüsüyle sıralı yazdırabiliriz.

result = soup.div   # ilk div etiketini döndürür.
result = soup.find_all("div")[0] # ilk div etiketini döndürür
result = soup.find_all("div")[1] # ikinci div etiketini döndürür

result = soup.find_all("div")[1].ul.li   # ikinci div etiketinin altındaki (ilk) ul etiketinin altındaki li etiketini (ilk) döndürür
result = soup.find_all("div")[1].ul.find_all("li")   # ikinci div etiketinin altındaki (ilk) ul etiketinin altındaki li etiketlerimi liste olarak döndürür

"""for r in result:   # find_all() metoduyla aldığımız verileri elbette bunları for döngüsüyle düzenli olarak alt alta yazdırabiliriz.
	print(r)"""

result = soup.div.findChildren()   # ilk div etiketinin children'larını (tüm alt etiketlerini) liste olarak döndürür

result = soup.div.findNextSibling()   # Aynı seviyedeki etiketler arasından sıradakini döndürür
result = soup.div.findPreviousSibling()   # Aynı seviyedeki etiketler arasından öncekini döndürür
result = soup.div.findNextSibling().findPreviousSibling()   # Aynısını döndürür :D

result = soup.find_all("a")   # a (link) etiketlerini liste olarak döndürür

"""for link in result:   # for etiketiyle sıralı yazdırır
	print(link)"""

"""for link in result:
	print(link.get("href"))"""   # .get() metodu, etiketin içerisindeki argumentler (argümanlar) arasından istenilenlerin içeriğini döndürür
#	                             # örneğin burada sadece linkler döndürülür

print(result)
