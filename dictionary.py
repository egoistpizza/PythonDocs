### Dict Veri Tipi ###

# key - value prensibinde çalışacağız.

# Yani verilerin birbirini temsil etmesini düşünün.
# Plaka numaraları gibi: 41 => Kocaeli, 34 => İstanbul, 35 => İzmir vb.

# Peki bunu Python'da nasıl yapacağız?
# İşte cevap :

'''dict = {key : value}'''

'''dict = { 'Kocaeli': 41, 'İstanbul': 34, 'İzmir': 35}
print(dict['Kocaeli'])
print(dict['İstanbul'])
print(dict['İzmir'])'''

'''dict = { 41: 'Kocaeli', 34: 'İstanbul', 35: 'İzmir'}
print(dict[41])
print(dict[34])
print(dict[35])'''

# Peki o zaman bu bilgileri kullanarak kullanıcıdan alınan plaka koduna ait şehri veren bir program yazalım.

'''dict = { 41: 'Kocaeli', 34: 'İstanbul', 35: 'İzmir'}
input = int(input('Plaka kodu giriniz : '))
print(dict[input])'''

# Peki dict veri tipindeki bir değişkene nasıl veri ekleme ve değiştirme nasıl yapılır ?
# Hadi sırayla gidelim, öncelikle dict veri tipindeki plaka numaralarımıza 22: 'Edirne' ve 26: 'Eskişehir' verilerini ekleyelim.

'''dict = { 41: 'Kocaeli', 34: 'İstanbul', 35: 'İzmir'}
dict[22] = 'Edirne'
dict[26] = 'Eskişehir'
print(dict)'''

# Şimdi de değiştirmeyi deneyelim.

'''dict = { 41: 'Kocaeli', 34: 'İstanbul', 35: 'İzmir'}
dict[41] = 'Kastamonu'
dict[34] = 'Ankara'
print(dict)'''

# Girilen kullanıcı adına ait unique id veren bir program yazalım.

'''users = {
    'MjolniR': 700765843834929174,
    'KvasiR': 709488319708397591,
    'BaldR': 500297618505859073,
    'HoduR': 159985870458322945,
    'Security': 651095740390834177
}
while True:
    nickname = input('Kullanıcı adı giriniz : ')
    print(users[nickname])'''

# Peki dict veri tipleri iç içe olabilir mi ? Elbette !

'''users = {
    'MjolniR': { 'uni': 700765843834929174, 'nick': 'MjolniR', 'code': '#4448' },
    'KvasiR': { 'uni': 709488319708397591, 'nick': 'KvasiR', 'code': '#2248' }
}
while True:
    nickname = input('Kullanıcı adı giriniz : ')
    info = input('İstenen bilgiyi giriniz (uni,nick,code) : ')
    print(users[nickname][info])'''