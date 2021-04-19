"""Convert date and time strings into datetime objects to perform nonstring operations on them. And back."""

from datetime import datetime

text = '2021-04-18'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
print(z - y)   # 1 day, 16:33:02.783097
print(z)       # 2021-04-19 16:35:50.368146
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)  # Monday April 19, 2021

# The performance of strptime() is quite bad due to the fact that it's written in pure Python
# Consider using a custom solution, for example
def parse_ymd(s: str) -> datetime:
    year, month, day = s.split('-')
    return datetime(int(year), int(month), int(day))
