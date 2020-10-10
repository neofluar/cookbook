# You want to create a dictionary, and you also want to control the insertion order of items.

from collections import OrderedDict


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['mir'] = 3
d['buz'] = 4
d['pak'] = 5
d['bok'] = 6
print(d)


import json
dump = json.dumps(d)
print('json dump', dump) # guaranty of order keeping when serialized


# methods specialized for rearranging dictionary order
print('Must be bok', d.popitem())
print('Must be pak', d.popitem())
print('Must be foo', d.popitem(last=False))

d.move_to_end('bar')
print('Must be bar', d.popitem())
d.move_to_end('buz', last=False)
print('Must be buz', d.popitem(last=False))

print(d)
