# döviz çevirme uygulaması

# ---- exchangeratesapi.io bilgileri ----
# mail: brenner.conlee@orperfect.com
# passwd: .kRJ<"^2_wCB[5?]
# api key: 74bcf0935d9174fb8741c8c91a2482ac
# ---- endpoints ----
# http://api.exchangeratesapi.io/v1/latest?access_key=74bcf0935d9174fb8741c8c91a2482ac
# -------------------

import requests
import json
import time

def menu():
	print("""
		| --------- EXCHANGE RATES API --------- |
		| KUR DÖNÜŞÜM HİZMETLERİNE HOŞ GELDİNİZ! |
		| -------------------------------------- |\n
		Lütfen yapmak istediğiniz işlemi seçin:
		1 - Para birimi dönüştür
		2 - Evrensel para birimi sembollerini görüntüle
		3 - Bağlantıyı kontrol et
		q - Çıkış yap
		""")

startTime = time.time()     # Start

currentRate = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=74bcf0935d9174fb8741c8c91a2482ac")

finishTime = time.time()    # Finish

currentRateDict = json.loads(currentRate.text)

while True:
	menu()
	option = input()
	if option == "q":
		break
	else:
		if option == "1":
			currentUnit = input("\nLütfen elinizdeki para birimini giriniz: ")
			targetUnit = input("Lütfen hedef para birimini giriniz: ")
			currentAmount = float(input("Lütfen elinizdeki para miktarını giriniz: "))
			base = currentRateDict["rates"][currentUnit]
			currentToEur = currentAmount / base
			targetRate = currentRateDict["rates"][targetUnit]
			result = currentToEur * targetRate
			print(result)
		elif option == "2":
			with open("currencies.json",encoding="utf-8") as file:
				unitCodes = json.load(file)
				for code in unitCodes:
					unit = unitCodes[code]
					print(code + ": " + unit)
		elif option == "3":
			if currentRateDict["success"]:
				print("API bağlantısı sağlandı!")
				ping = finishTime - startTime
				print(f"Ping = {ping} saniye")
			else:
				print("API bağlantısı sağlanamadı!")
