# Bankamatik Uygulaması

import sys

accountA = {
    'user': 'Fırat Kaya',
    'acno': '0000000001',
    'balance': 6712.49,
    'limit': 10000,
    'mail': 'firatkaya@mail.com',
    'phone': '+90-555-555-00-01'
}
accountB = {
    'user': 'Hale Gündüz',
    'acno': '0000000002',
    'balance': 12956.75,
    'limit': 30000,
    'mail': 'halegunduz@mail.com',
    'phone': '+90-555-555-00-02'
}
accountC = {
    'user': 'Dilek Yan',
    'acno': '0000000003',
    'balance': 3781.93,
    'limit': 5000,
    'mail': 'dilekyan@mail.com',
    'phone': '+90-555-555-00-03'
}


def greeting():
    print('''
    |---------------------------|
    |ABC Bankamatik Hizmetlerine|
    |      Hoş Geldiniz !       |
    |---------------------------|
    ''')


def paraCek(account, value):
    print(f"Sayın {account['user']}, para çekme menüsüne hoş geldiniz.")
    if account['balance'] >= value:
        print('Miktar ONAYLANDI.')
        print('İşlem başarıyla tamamlandı.')
        account['balance'] = account['balance'] - value
        print(f"\nKalan bakiyeniz {account['balance']} TL'dir.")
    else:
        print('Yetersiz bakiye.')
        print(f"Mevcut bakiyeniz {account['balance']} TL'dir.")
        sys.exit(0)
        raise SystemExit


def paraYatir(account, value2):
    print(f"Sayın {account['user']}, para yatırma menüsüne hoş geldiniz.")
    if account['limit'] >= value2 + account['balance']:
        print('Limit ONAYLANDI.')
        print('İşlem başarıyla tamamlandı.')
        account['balance'] = account['balance'] + value2
        print(f"\nMevcut bakiyeniz {account['balance']} TL'dir.")
    else:
        print('Yetersiz limit.')
        print(f"Mevcut limitiniz {account['limit']} TL'dir.")
        sys.exit(0)
        raise SystemExit


def bakiyeSorgula(account):
    print(f"Sayın {account['user']}, bakiye sorgulama menüsüne hoş geldiniz.")
    print(f"Mevcut bakiyeniz {account['balance']} TL'dir.")


greeting()
log = (input("\nHesap keyword'ünü giriniz: "))
logDict = {
    'accountA': accountA,
    'accountB': accountB,
    'accountC': accountC
}
login = logDict[log]
req = input(
        'Gerçekleştirmek istediğiniz işlemi belirtiniz (paraCek,paraYatir,bakiyeSorgula): ')
if req == 'paraCek':
    value = float(input('Çekmek istediğiniz miktarı giriniz :'))
    paraCek(login, value)
elif req == 'paraYatir':
    value2 = float(input('Yatırmak istediğiniz miktarı giriniz :'))
    paraYatir(login, value2)
elif req == 'bakiyeSorgula':
    bakiyeSorgula(login)
else:
    print('Çıkış yapılmıştır.')
    sys.exit(0)
    raise SystemExit
