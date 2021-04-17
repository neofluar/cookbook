"""Simple time conversions with datetime and dateutil"""

# 1. Time interval representation
from datetime import timedelta
a = timedelta(days=2, hours=6)         # the hours and minutes attributes will be internally converted to seconds
b = timedelta(hours=4.5)
c = a + b
print(c)                               # 2 days, 10:30:00
print(c.days)                          # 2 - days attribute of timedelta instance
print(c.seconds)                       # 37800 - seconds attribute of timedelta instance
print(c.seconds / 3600)                # 10.5  - no access to hours and minutes attributes after timedelta initialization
print(c.total_seconds() / 3600)        # 58.5 - converts timedelta instance to total hours
print(c.days * 24 + c.seconds / 3600)  # 58.5 - another way to convert timedelta instance to total hours

# 2. Specific date and time representation
from datetime import datetime
a = datetime(2021, 3, 16)
b = datetime(2021, 12, 21)
d = b - a
now = datetime.today()
e = datetime(2012, 3, 1)
f = datetime(2012, 2, 28)

print(a + timedelta(days=10))       # 2021-03-26 00:00:00
print(d.days)                       # 280
print(now)                          # 2021-04-16 09:25:52.148100
print(now + timedelta(minutes=10))  # 2021-04-16 09:35:52.148100
print((e - f).days)                 # 2 - datetime is aware of leap years

# 3. More complex date manipulation (dateutil)
a = datetime(2021, 3, 16)
try:
    b = a + timedelta(month=1)
except TypeError:
    print('timedelta has no month attribute')

from dateutil.relativedelta import relativedelta
print(a + relativedelta(months=4))  # 2021-07-16 00:00:00

b = datetime(2021, 12, 21)
print(b - a)                # 280 days, 0:00:00 - timedelta object
print(relativedelta(b, a))  # relativedelta(months=+9, days=+5)
