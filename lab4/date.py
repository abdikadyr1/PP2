import datetime
print("#1")    
tday = datetime.date.today()
tdelta = datetime.timedelta(days=5)
print(tday - tdelta)

yestday = tday - datetime.timedelta(days=1)
tmorrow = tday + datetime.timedelta(days=1)
print("#2")
print(f"yesterday: {yestday} {"\n"}today: {tday} {"\n"}tomorrow: {tmorrow}")
print("#3")
cur = datetime.datetime.now()
print(cur.strftime("%c"))
print("#4")
date1 = datetime.date(2006, 5, 16)
date2 = datetime.date.today()
still_alive = date2 - date1
print(still_alive.total_seconds())