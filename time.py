import datetime
print ("The represented date is : ")
print (datetime.date(1997,4,1))
print(
    datetime.datetime.fromtimestamp(1503312054).strftime('%Y-%m-%d %H:%M:%S')
)