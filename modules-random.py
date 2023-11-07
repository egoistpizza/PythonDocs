# Random modülü hakkında dokümantasyon.

'''
import random

commands = dir(random)
help = help(random)

rastgeleSayi = random.random()  # 0.0 - 1.0 arasında bir sayı verir.
rastgeleSayi100 = random.random() * 100  # 0.0 - 100.0 arasında bir sayı verir.
araliktaSayi = random.uniform(5, 6)  # 5.0 - 6.0 arasında bir sayı verir.
araliktaInt = random.randint(315, 400)  # 315 ile 400 arasında bir int verir.

print(rastgeleSayi, rastgeleSayi100, araliktaSayi, araliktaInt)
'''

###

'''
import random

greeting = 'hello there'
names = ['ali', 'yağmur', 'deniz', 'cenk']

# uzun yol - listeden eleman seçer.
listedenSec = names[random.randint(0, len(names)-1)]
# kısa yol - listeden eleman seçer.
listedenSec = random.choice(names)
# string'den harf seçer.
harfSec = random.choice(greeting)

liste = list(range(10))  # 0'dan 10'a kadar sayıları bir listeye aktarır.
random.shuffle(liste)  # listedeki elemanları karıştırır ! :)

liste1 = range(100)  # 0'dan 100'e kadar olan sayıları tutar.
ornekAl = random.sample(liste1, 3)  # bu aralıktaki sayılardan 3 tane çeker.
ornekAl1 = random.sample(names, 2)  # listedeki isimlerden 2 tane çeker.

print(listedenSec, harfSec, liste, ornekAl, ornekAl1)
'''
