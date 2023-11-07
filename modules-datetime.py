# DATETIME MODULÜ:
# Dokümanlar: https://docs.python.org/3/library/datetime.html
# Dokümanlar: https://www.w3schools.com/python/python_datetime.asp

"""
Directive 	Description 	                        Example 	

%a 	        Weekday, short version 	                Wed 	
%A 	        Weekday, full version 	                Wednesday 	
%w 	        Weekday as a number 0-6, 0 is Sunday 	3 	
%d 	        Day of month 01-31 	                    31 	
%b 	        Month name, short version 	            Dec 	
%B 	        Month name, full version 	            December 	
%m 	        Month as a number 01-12 	            12 	
%y 	        Year, short version, without century 	18 	
%Y 	        Year, full version 	                    2018 	
%H 	        Hour 00-23 	                            17 	
%I 	        Hour 00-12 	                            05 	
%p 	        AM/PM 	                                PM 	
%M 	        Minute 00-59 	                        41 	
%S 	        Second 00-59 	                        08 	
%f 	        Microsecond 000000-999999 	            548513 	
%z 	        UTC offset 	                            +0100 	
%Z 	        Timezone 	                            CST 	
%j 	        Day number of year 001-366 	            365 	
%U 	        Week number of year, Sunday as the first day of week, 00-53 	52 	
%W 	        Week number of year, Monday as the first day of week, 00-53 	52 	
%c 	        Local version of date and time 	        Mon Dec 31 17:41:00 2018 	
%C 	        Century 	                            20 	
%x 	        Local version of date 	                12/31/18 	
%X 	        Local version of time 	                17:41:00 	
%% 	        A % character 	                        % 	
%G 	        ISO 8601 year 	                        2018 	
%u 	        ISO 8601 weekday (1-7) 	                1 	
%V 	        ISO 8601 weeknumber (01-53) 	        01
"""


from datetime import datetime       # datetime modülü date ve time modüllerini kapsıyor. Direkt ikisini de içe aktardık.
from datetime import timedelta      # timedelta modülü tarih üzerinden işlem yapmamızı sağlar.
# from datetime import date
# from datetime import time

# import datetime

"""result = dir(datetime)"""
# result = dir(datetime.time)
# result = dir(datetime.date)

simdi = datetime.now()             # O anki gün ay yıl saati verir.
simdi = datetime.today()           # Aynısını yapar.

result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,"%Y")
result = datetime.strftime(simdi,"%X")
result = datetime.strftime(simdi,"%D")
result = datetime.strftime(simdi,"%A")
result = datetime.strftime(simdi,"%B")
result = datetime.strftime(simdi,"%H")
result = datetime.strftime(simdi,"%M")
result = datetime.strftime(simdi,"%Y %B %A")

t = "21 Nisan 2022"
gun, ay, yil = t.split()
print(gun)
print(ay)
print(yil)

t = "21 April 2022 hour 01:27:30"
dt = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")   # String'i datetime olarak atar, yerleştirir.
dt = dt.year

birthday = datetime(1999,1,19,12,30,00)

result = datetime.timestamp(birthday)   # saniye
result = datetime.fromtimestamp(result)   # saniye -> datetime
result = datetime.fromtimestamp(0)   # 1970-01-01 02:00:00

result = simdi - birthday   # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)
# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes=10)

# result = simdi - timedelta(days=10)

print(result)

print(birthday)

print(dt)
