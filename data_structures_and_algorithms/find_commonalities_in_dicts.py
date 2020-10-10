# You have 2 dictionaries and want to find out what they might have in common.

a = {'x' : 1, 'y': 2, 'z': 3}
b = {'w' : 10, 'y': 2, 'x': 11}

# ATTENTION: that doesn't work on values-view objects
print(a.keys() & b.keys())   # common keys {'x', 'y'}
print(a.keys() - b.keys())   # keys in a that are not in b {'z'}
print(a.items() & b.items()) # common key-value pairs {('y', 2),}

# make a new dict with certain keys removed
print({key: a[key] for key in a.keys() - {'z', 'w'}}) # {'x': 1, 'y': 2}
