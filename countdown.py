from datetime import date, datetime

x=datetime.today()
y=x.replace(day=x.day+1, hour=3, minute=1, second=0)
delta_t=y-x 
secs=delta_t.seconds+1

second = (secs % 60)
minute = (secs / 60) % 60
hour = (secs / 3600)
day = (secs / 3600*24)

print("Seconds : %s" % (second))
print("Minute: %s" % (minute))
print("Hour: %s" % (hour))
print('Day: %s' % (day))

print('Time left is %s:%s:%s') % (day, hour, minute, second)
