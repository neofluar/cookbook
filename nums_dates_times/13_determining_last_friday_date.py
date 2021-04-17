"""A general solution for finding a date for the last occurrence of a day of the week"""

# 1. Using datetime
from typing import Optional
from datetime import datetime
from datetime import timedelta

WEEK_DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


def get_previous_by_day(day_name: str, start_date: Optional[datetime] = None) -> datetime:
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = WEEK_DAYS.index(day_name)
    if (days_ago := (7 + day_num - day_num_target) % 7) == 0:
        days_ago = 7
    return start_date - timedelta(days=days_ago)


print(datetime.today())                                       # 2021-04-17 18:49:44.959160
print(get_previous_by_day('Monday'))                          # 2021-04-12 18:49:44.959179
print(get_previous_by_day('Saturday'))                        # 2021-04-10 18:49:44.959190
print(get_previous_by_day('Sunday'))                          # 2021-04-11 18:49:44.959197
print(get_previous_by_day('Sunday', datetime(2012, 12, 21)))  # 2012-12-16 00:00:00

# 2. Using dateutil
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

date = datetime.today()
print(date)                                  # 2021-04-17 19:01:41.655106
print(date + relativedelta(weekday=FR))      # 2021-04-23 19:01:41.655106 - the next Friday
print(date + relativedelta(weekday=FR(-1)))  # 2021-04-16 19:01:41.655106 - the last Friday
