# Dokümanlar: https://docs.python.org/3/howto/regex.html
# Dokümanlar: https://www.w3schools.com/python/python_regex.asp
# Dokümanlar: https://www.geeksforgeeks.org/python-regex/

import re       # modülümüzü içe aktarıyoruz.

result = dir(re)

# ---------- RE MODULE ----------

str = "Python Kursu: Python Programlama Rehberi | 40 Saat"

# re.findall()

"""result = re.findall("Python",str)    # verilen kelimeyi bulur ve liste şeklinde döndürür: ['Python', 'Python']
 result = len(result)"""                # liste eleman sayısı, stringdeki aranan öge sayısı: 2

# re.split()         # verilen parametreden stringi böler ve liste olarak ayırır.

"""result = re.split(" ",str)
result = re.split("R",str)"""

# re.sub()       # 1. parametrede verilenleri bulup 2. parametredeki karakterle değiştirir.

"""result = re.sub(" ","-",str)
result = re.sub("\s","-",str)"""         # \s = boşluk

# re.search()

# result = re.search("Python",str)
# <re.Match object; span=(0, 6), match='Python'>

# result = result.span()
# (0, 6)

# result = result.start()      # 0
# result = result.end()        # 6
# result = result.group()      # Python
# result = result.string       # Python Kursu: Python Programlama Rehberi | 40 Saat

# ---------- REGULAR EXPRESSİON ----------

"""
    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.
         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches
         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]      # 0-3 arası + 9 ! 
         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.
"""
result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[0-5]",str)
result = re.findall("[^abc]",str)
result = re.findall("[^0-9]",str)
"""
    . - Her hangi bir tek karakteri belirtir.
        .. => a    : No match
              ab   : 1 match
              abc  : 1 match      # ab değeri döner
              abcd : 2 matches    # ab ve cd döner
"""
result = re.findall("...",str)
result = re.findall("Py..on",str)
"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?
    ^a => a:    1 match
          abc:  1 match
          bac:  No match
"""
result = re.findall("^P",str)
result = re.findall("^K",str)
"""
    $ - Belirtilen karakterle bitiyor mu ?
    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 
"""
result = re.findall("t$",str)
result = re.findall("a$",str)
result = re.findall("Saat$",str)
"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
result = re.findall("Pytho*n",str)
result = re.findall("Sa*t",str)
"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
result = re.findall("Sa+t",str)
result = re.findall("Pytho+n",str)
result = re.findall("",str)
"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.
        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""
result = re.findall("Sa?t",str)
result = re.findall("Saa?t",str)
"""
    {} - Karakter sayısını kontrol eder.
        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
result = re.findall("a{2}",str)
result = re.findall("[0-9]{2}",str)
"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
        a|b => a ya da b
            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""
result = re.findall("a|b",str)
"""
    () - gruplamak için kullanılır.
         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""
result = re.findall("(a|b|c)t",str)
"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.
    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı
        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)
    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı
    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?
    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50
    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi   
"""

result = re.findall("\APython",str)
result = re.findall("Saat\Z",str)

passwd = "(=)Ujkba65741evı=("
result = re.findall("\W",passwd)
result = re.findall("\w",passwd)

print(result)
