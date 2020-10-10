# You want to sort objects of the same class, but they don’t natively support comparison operations.

from operator import attrgetter

class User:

    def __init__(self, uid, first, last):
        self.uid = uid
        self.first = first
        self.last = last

    def __repr__(self):
        return f'{self.uid}-{self.first}-{self.last}'

records = [
    User(1003, 'Brian', 'Jones'),
    User(1001, 'David', 'Cleese'),
    User(1002, 'John', 'Beazley'),
    User(1004, 'Big', 'Jones'),
]

records_by_uid = sorted(records, key=attrgetter('uid'), reverse=True)
print(records_by_uid)

records_by_first_last = sorted(records, key=attrgetter('first', 'last'), reverse=True)
print(records_by_first_last)

minuid_record = min(records, key=attrgetter('uid'))
print(minuid_record)
