# You have a list of dictionaries and you would like to sort the entries according to one
# or more of the dictionary values.

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname')) # can accept multiple keys as a basis of comparision
print(rows_by_lfname)

maxuid_row = max(rows, key=itemgetter('uid'))
print(maxuid_row)

# you can use a lambda function instead (a bit slower)
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))

minfnamelen_row = min(rows, key=lambda r: len(r['fname']))
print(minfnamelen_row)
