# themoviedb.otg => film ve dizi arşivi
# themoviedb api'ını kullan
# Anahtar kelimeye göre arama
# En popüler filmler listesi
# Vizyondaki film listesi


import requests
import json

class Movie:
	def __init__(self):
		self.api_key = "YOUR_KEY_HERE"
		self.api_url = "https://api.themoviedb.org/3"

	def movieSearch(self, keyword):
		response = requests.get(f"{self.api_url}/search/movie?api_key={self.api_key}&language=en-US&query={keyword}&page=1&include_adult=true")
		result = response.json()
		for counter in range(10):
			results = result["results"]
			movie = results[counter]
			title = movie["original_title"]
			overview = movie["overview"]
			print(f"\nFilm Adı: {title}, Film Açıklaması: {overview}")

	def populerMovies(self):
		response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
		result = response.json()
		for counter in range(10):
			results = result["results"]
			movie = results[counter]
			title = movie["original_title"]
			overview = movie["overview"]
			print(f"\nFilm Adı: {title}, Film Açıklaması: {overview}")

	def nowPlaying(self):
		response = requests.get(f"{self.api_url}/movie/now_playing?api_key={self.api_key}&language=en-US&page=1")
		result = response.json()
		for counter in range(10):
			results = result["results"]
			movie = results[counter]
			title = movie["original_title"]
			overview = movie["overview"]
			print(f"\nFilm Adı: {title}, Film Açıklaması: {overview}")

movie = Movie()

while True:
	secim = input("\n1 - Film Araması\n2 - Popüler Filmler\n3 - Vizyondaki Filmler\n4 - Çıkış\nSeçiminiz: ")

	if secim == "4":
		break

	else:

		if secim == "1":
			keyword = input("Film adı giriniz: ")
			try:
				movie.movieSearch(keyword)
			except IndexError:
				pass

		elif secim == "2":
			movie.populerMovies()

		elif secim == "3":
			movie.nowPlaying()

		else:
			print("Yanlış tuşlama yaptınız.")
			break
			
