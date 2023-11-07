# Hesap makinesi
def topla(sayi1, sayi2):
    return sayi1 + sayi2
def cikar(sayi1, sayi2):
    return sayi1 - sayi2
def carp(sayi1, sayi2):
    return sayi1 * sayi2
def bol(sayi1, sayi2):
    return sayi1 / sayi2
def kalan(sayi1, sayi2):
    return sayi1 % sayi2

print("""
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
5. Kalan
""")

islem = input("İşlem seçiniz: ")

sayi1 = int(input("Birinci sayı: "))
sayi2 = int(input("İkinci sayı: "))

if islem == "1":
    print(topla(sayi1, sayi2))
elif islem == "2":
    print(cikar(sayi1, sayi2))
elif islem == "3":
    print(carp(sayi1, sayi2))
elif islem == "4":
    print(bol(sayi1, sayi2))
elif islem == "5":
    print(kalan(sayi1, sayi2))
else:
    print("Geçersiz işlem")
