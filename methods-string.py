# Daha fazla bilgi için <https://www.w3schools.com/python/python_ref_string.asp>

customMessage = 'UpperLower v0.1 yazılımına hoş geldiniz.'
# format = 'UpperLower {} v0.1 yazılımına {} hoş geldiniz.'.format(1,2) # Verilen ifadedeki köşeli parantezlere sırasıyla verilen parametredeki ifadeleri getirir.
# upper = customMessage.upper() # Tüm karakterleri büyük harfe dönüştürür.
# lower = customMessage.lower() # Tüm karakterleri küçük harfe dönüştürür.
# title = customMessage.title() # Tüm kelimelerin ilk harfleri büyük yazılır. Diğer tüm karakterler küçültülür.
# capitalize = customMessage.capitalize() # [0] index'indeki karakter büyütülür. Diğer tüm karakterler küçültülür.
# strip = customMessage.strip() # String ifadenin baş ve sonundaki boşlukları siler. lstrip (soldan sil) ve rsplit (sağdan sil) metotları mevcuttur. Parametre bölümüne tırnak içerisinde silmek istediğimiz karakterler birer kez yazılabilir.
# split = customMessage.split() # String ifadeyi istenen karakterlerden bölerek ve indexlenebilir hale getirir.
# join = ' '.join(customMessage) # Liste halindeki bölünmüş (splitted) ifadeleri istenen karakterle birleştirir.
# find = customMessage.find('UpperLower') # String içerisinde bulmak istediğimiz kelimenin ilk harfinin index'ini verir. rfind ve lfind metotları mevcuttur, bu sayede soldan sağa veya sağdan sola arama yapılabilir.
# index = customMessage.index('UpperLower') # Find metoduna alternatiftir. Aynı şekilde rindex ve lindex metotları mevcuttur. Farklı yönü, eğer aradığınız ifade string içerisinde bulunmuyorsa ValueError alırsınız.
# startswith = customMessage.startswith('U') # String ifadenin soldan sağa indexlerindeki karakterlerin verdiğimiz parametre olup olmadığını boolean veri tipinde yansıtır.
# endswith = customMessage.endswith('.') # String ifadenin sağdan sola indexlerindeki karakterlerin verdiğimiz parametre olup olmadığını boolean veri tipinde yansıtır.
# replace = customMessage.replace('UpperLower','LowerUpper') # İstenen karakter dizisini verilen parametredeki ifadeyle değiştirir. Yan yana eklenebilir (Örn. customMessage.replace(*,*).replace(-,-).replace(\,\)). İşlemin kaç kez yapılmasını istediğimizi 3. parametre olarak verebiliriz.
# center = customMessage.center(100,'-') # String ifadeyi verilen parametre boyutundaki bir alanda boşluklar yardımıyla ortalar. 2. parametre boşlukları istenen karakterlere dönüştürür. ljust (sola yasla) ve rjust (sağa yasla) metotları mevcuttur.
# isalpha = customMessage.isalpha() # String ifadede bulunan karakterlerin tamamının harf olup olmama durumunu boolean veri tipinde verir.
# isdigit = customMessage.isdigit() # String ifadenin rakamlardan oluşup oluşmadığını boolean veri tipinde verir. Üslü sayıları da True kabul eder.
# isdecimal = customMessage.isdecimal() # String ifadenin tamamen rakamlardan oluşup oluşmadığını boolean veri tipinde verir.
# isnumeric = customMessage.isnumeric() # String ifadenin rakamlardan oluşup oluşmadığını boolean veri tipinde verir. Üslü sayıları ve kesirleri de True kabul eder.

print()