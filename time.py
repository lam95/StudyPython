import datetime, time
print ("The represented date is : ")
print(
    datetime.datetime.fromtimestamp(int("1284101485")).strftime('%Y-%m-%d %H:%M:%S')
)
local_time = time.localtime(int("1284101485"))
print(time.strftime("%Y-%m-%d %H:%M:%S", local_time))