import os
import datetime

result = dir(os)
result = os.name                                     # Kernel'i yazdırır

# Dizin işlemleri

# os.chdir("/home/egoist/Belgeler")                  # change directory
# os.chdir("..")
# os.chdir("../..")
# result = os.getcwd()                               # current working directory

# Klasör işlemleri

# os.mkdir("newDirectory")                           # make directory
# os.makedirs("newDirectory/yeniKlasor")             # make (sub) directories
# os.rename("newDirectory","yepisyeniKlasor")        # rename directories/files !!!
# os.rmdir("newDirectory3")                          # remove directory
# os.removedirs("newDirectory2/yeniKlasor")          # remove (sub) directories

# listeleme

# result = os.listdir()                              # list directory
# result = os.listdir("/home/egoist")                # list directory ...
"""for dosya in os.listdir():                        # sonu .py ile biten dosyaları döndür
	if dosya.endswith(".py"):
		print(dosya)"""

# stat - datetime: fromtimestamp

# result = os.stat("modules-datetime.py")            # dosya bilgileri
# result = result.st_size/1024                       # kb cinsinde veri döndürür, dosya boyutu
# result = datetime.datetime.fromtimestamp(result.st_ctime)      # dosyanın oluşturulma zamanını döndürür.
# result = datetime.datetime.fromtimestamp(result.st_atime)      # son erişim tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)      # değiştirilme tarihi

# os.system("idle")                                  # program çalıştır

# path class !
# Dizin yönetimi

# result = os.path.abspath("modules-os.py")                                             # /home/egoist/Belgeler/PythonDocs/modules-os.py
# result = os.path.dirname("/home/egoist/Belgeler/PythonDocs")                          # /home/egoist/Belgeler
# result = os.path.dirname(os.path.abspath("modules-os.py"))                            # /home/egoist/Belgeler/PythonDocs
# result = os.path.exists("modules-os.py")                                              # varsayılan dizinde x dosyası var mı?
# result = os.path.exists("projects")                                                   # varsayılan dizinde x klasörü var mı?
# result = os.path.isdir("/home/egoist/Belgeler")                                       # x dizini bir klasör mü?
# result = os.path.isfile("/home/egoist/Belgeler/PythonDocs/modules-os.py")             # x dizini bir dosya mı?
# result = os.path.join("/home/egoist/Belgeler","newDirectory","deneme1")               # ögeleri birleştir ve adres oluştur
# result = os.path.split("/home/egoist/Belgeler")                                       # ögeleri ayır
# result = os.path.splitext("modules-os.py")                                            # uzantı ve dosya adını ayır
# result = result[0]                                                                    
# result = result[1]                                                                    

print(result)