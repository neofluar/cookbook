# You have a sequence of dictionaries or instances and you want to iterate over the data
# in groups based on the value of a particular field, such as date.

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

# Sort by the desired field first, because groupby() only examines consecutive items
rows.sort(key=itemgetter('date'))

# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('    ', i)

# if your goal is to simply group the data together by dates into a larger data structure
from collections import defaultdict

date_rows = defaultdict(list)
for row in rows:
    date_rows[row['date']].append(row)

date = '07/01/2012'
print('\n\n', date, sep='')
for r in date_rows[date]:
    print(r)
