# You have data inside of a sequence, and need to extract values or reduce the sequence using some criteria.

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# the easiest way
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])
print([n if n > 0 else 0 for n in mylist])
print([n if n < 0 else 0 for n in mylist])

# in the case of a large input use a generator
generator = (n for n in mylist if n > 0)
print([n for n in generator])

# in the case of complicated filtering criteria use built-in filter() -> iterator
values = ['1.5', '2', '-3', '-', '4', 'N/A', '5']

def is_int(n):
    try:
        _ = int(n)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)  # prints ['2', '-3', '4', '5']

# for numpy-like boolean indexing use itertools.compress() -> iterator
from itertools import compress

addresses = ['5412 N CLARK', '5148 N CLARK', '5800 E 58TH',
             '2122 N CLARK', '5645 N RAVENSWOOD', '1060 W ADDISON',
             '4801 N BROADWAY', '1039 W GRANVILLE']
counts = [0, 3, 10, 4, 1, 7, 6, 1]

morethan5 = [n > 5 for n in counts]
print(list(compress(addresses, morethan5)))  # prints ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
