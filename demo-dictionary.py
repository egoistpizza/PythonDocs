'''ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'tel': '530 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'tel': '530 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'tel': '530 000 00 03'
    }
}'''

# 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içerisinde saklayın.

'''ogrenciler = {}
number = input('Öğrenci Numarası: ')
name = input('Öğrenci Adı: ')
surname = input('Öğrenci Soyadı: ')
phone = input('Öğrenci Telefon: ')

ogrenciler.update({
    number: {
        'Ad': name,
        'Soyad': surname,
        'Telefon': phone
    }
})
print(ogrenciler)'''

# 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

'''inPut0 = input('\nÖğrenci Numarası Giriniz: ')
inPut1 = input('İstenen Veriyi Giriniz: ')
print(ogrenciler[inPut0][inPut1])'''