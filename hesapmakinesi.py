# gelişmiş hesap makinesi programı
# python3 hesapmakinesi.py

import sys

print("""
    1. Toplama
    2. Çıkarma
    3. Çarpma
    4. Bölme
    5. Çıkış
""")

while True:
    islem = input("İşlem seçiniz: ")
    if islem == "1":
        sayi1 = int(input("1. sayı: "))
        sayi2 = int(input("2. sayı: "))
        print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
    elif islem == "2":
        sayi1 = int(input("1. sayı: "))
        sayi2 = int(input("2. sayı: "))
        print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
    elif islem == "3":
        sayi1 = int(input("1. sayı: "))
        sayi2 = int(input("2. sayı: "))
        print(sayi1, "*", sayi2, "=", sayi1 * sayi2)
    elif islem == "4":
        sayi1 = int(input("1. sayı: "))
        sayi2 = int(input("2. sayı: "))
        print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
    elif islem == "5":
        print("Programdan çıkılıyor...")
        sys.exit()
    else:
        print("Geçersiz işlem...")
        continue
    devam = input("Devam etmek istiyor musunuz? (e/h): ")
    if devam == "e":
        continue
    elif devam == "h":
        print("Programdan çıkılıyor...")
        sys.exit()
    else:
        print("Geçersiz işlem...")
        continue