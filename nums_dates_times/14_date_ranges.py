"""An efficient way to calculate date ranges"""

import calendar
from datetime import date, timedelta


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(year=start_date.year, month=start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


def date_range_generator(start, stop, step):
    while start < stop:
        yield start
        start += step


if __name__ == '__main__':
    first_day, last_day = get_month_range()
    print(first_day, last_day)  # 2021-04-01 2021-05-01
    for d in date_range_generator(first_day, last_day, timedelta(days=1)):
        print(d)
