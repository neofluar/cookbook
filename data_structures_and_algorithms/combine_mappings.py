# You have multiple dictionaries or mappings that you want to logically combine into a
# single mapping to perform certain operations, such as looking up values or checking
# for the existence of keys

from collections import ChainMap

a = {'x': 11, 'z': 33}
b = {'y': 22, 'z': 44}

c = ChainMap(a, b) # the order matters!
print(c['y'])  # prints 22 from b
print(c['z'])  # prints 33 from a

print(len(c))  # prints 3
print(list(c.keys()))
print(list(c.values()))

# Operations that mutate the mapping always affect the first one
c['z'] = 100
c['w'] = 50
print(c)
del c['x']
print(a)

# ChainMap's methods
values = ChainMap()
values['x'] = 1

# 1. add new mappings to the chain
values = values.new_child()
values['x'] = 2

values = values.new_child()
values['x'] = 3
print(values)  # prints ChainMap({'x': 3}, {'x': 2}, {'x': 1})
print(values['x'])  # prints 3 (the last added)

# 2. discard the last added mapping
values = values.parents
print(values)  # prints ChainMap({'x': 2}, {'x': 1})
print(values['x'])  # prints 2 (the pre-last added)


# you can use a dict merging (memory consumption!) + the changes don’t get reflected in the merged dictionary
a = {'x': 11, 'z': 33}
b = {'y': 22, 'z': 44}
m = dict(b)  # a brilliant way to ensure creating a new dict
m.update(a)
print(m['z'])  # prints 33