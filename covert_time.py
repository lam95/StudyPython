import datetime, time
from datetime import date

print ("The represented date is : ")
unix_time = int("1284101485")
local_time = datetime.datetime.fromtimestamp(int("1284101485")).strftime('%Y-%m-%d %H:%M:%S')
print(local_time)
print(unix_time)
unix_time = int(time.mktime(datetime.datetime.strptime(local_time, "%Y-%m-%d %H:%M:%S").timetuple()))
print(unix_time)
