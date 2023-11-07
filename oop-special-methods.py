# ----- OOP-SpecialMethods ----- #
# For more info, check https://www.informit.com/articles/article.aspx?p=453682&seqNum=6 !

class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = f"{duration // 60}h {duration % 60}min"
        self.intDuration = duration
    
    def __str__(self):                                        # method 1 (__str__())
       return f"{self.title} by {self.director} ."
    
    def __len__(self):                                        # method 2 (__len__())
        return self.intDuration

    def __del__(self):                                        # method 3 (__del__())
        print(f"{self.title} has been deleted .")

movie0 = Movie("Pianist","Roman Polanski",150)

# ---------- #
# __str__(): Oluşturduğumuz class'a ait bir nesneyi print() metoduyla ekrana yazdırmak istediğimizde,
# str() metoduyla dönüştürmeyi denesek de bellek üzerindeki referans numarası ekrana yazdırılır.
# Bunu özelleştirmek için class'ta __str__() metodu tanımlarız ve bu sayede belirlediğimiz objenin print
# edilmesi durumunda return edilecek veriyi kendimiz hazırlayabiliriz .
# ---------- #
# __len__(): Oluşturduğumuz class'a ait objenin üzerinde len() metodunu kullandığımızda bir hata
# mesajıyla karşılaşırız. Bunun yerine __len__() metodu ile istediğimiz return verisini ayarlayarak
# obje üzerinde len() kullanılması durumunda yansıtılacak bilgiyi özelleştirebiliriz.
# ---------- #
# __del__(): Oluşturduğumuz class'a ait değişkenin üzerinde del işlemini kullanarak onu sildiğimizde
# (örn. del movie0) yapılacak işlemleri özelleştirebiliriz. Örneğin ögenin silindiğine dair bir
# bilgilendirme mesajı print edebiliriz. Not: Obje kullanıldıktan sonra RAM üzerinden silindiği
# için işlemimizin sonunda __del__() metodu daima çalışır.
# ---------- #