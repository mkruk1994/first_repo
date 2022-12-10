import datetime
import time

today = datetime.date.today()
#print(type(today))
#print(today)

data1 = today.strftime('Dzisiaj jest %d dzień %m miesiąca')
data2 = today.strftime('%d - %m - %y')
#print(data1)
#print(data2)

#print(type(now))
#print(now)

#my_now = now.strftime('')

name = "report.txt"
for i in range (10):
    now = datetime.datetime.now()
    my_now2 = now.strftime('%H%M%S')
    print(name[0:6] + my_now2 + name[6:])
    time.sleep(2)