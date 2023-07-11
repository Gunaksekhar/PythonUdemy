import datetime
mytime = datetime.time(9, 5, 2,6)
print(mytime)
print(mytime.hour)

print()

#now
rnow = datetime.datetime.now()
print("Right Now: ", rnow)

#today
Today = datetime.datetime.today()
print("Today time: ",Today, "\n")

from datetime import datetime
mydatetime = datetime(2020,9,5,9,10,29)
print("mydatetime: ", mydatetime,"\n")