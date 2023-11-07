# tbody (lister-list) -> tr -> 2. td -> a:
# title= oyuncu kadrosu
# a etiket ismi= film ismi

# tbody -> tr -> 2. td -> span:
# span = film çıkış tarihi

# tbody -> tr -> 3. td -> strong:
# title= ... based on ... user ratings
# strong etiket ismi -> IMDb puanı

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr")   # [Liste döndürür]

counter = 0

for movie in list:
	titleColumn = movie.find("td", {"class":"titleColumn"})
	movieName = titleColumn.a.text
	releaseDate = titleColumn.span.text
	ratingColumn = movie.find("td", {"class":"ratingColumn imdbRating"})
	rating = ratingColumn.strong.text
	rating_str = ratingColumn.strong.get("title")
	counter += 1

	print(f"{str(counter).ljust(3)} - {str(movieName).ljust(100)} - {releaseDate}, {rating_str}")
print("")