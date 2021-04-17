"""A general solution for finding a date for the last occurrence of a day of the week"""

from datetime import datetime
from datetime import timedelta

WEEK_DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


def get_previous_by_day(day_name, start_date=None) -> datetime:
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = WEEK_DAYS.index(day_name)
    if (days_ago := (7 + day_num - day_num_target) % 7) == 0:
        days_ago = 7
    return start_date - timedelta(days=days_ago)


if __name__ == '__main__':
    print(datetime.today())                 # 2021-04-17 18:49:44.959160
    print(get_previous_by_day('Monday'))    # 2021-04-12 18:49:44.959179
    print(get_previous_by_day('Saturday'))  # 2021-04-10 18:49:44.959190
    print(get_previous_by_day('Sunday'))    # 2021-04-11 18:49:44.959197
