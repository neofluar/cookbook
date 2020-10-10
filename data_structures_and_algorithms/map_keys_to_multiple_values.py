# You want to make a dictionary that maps keys to more than one value.

from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
print("d['a'] =", d['a'])

s = defaultdict(set)
s['b'].add(4)
s['b'].add(5)
print("s['b'] =", s['b'])

print('ATTANTION: unassigned key will be initiated =', s['no_such_key'])
