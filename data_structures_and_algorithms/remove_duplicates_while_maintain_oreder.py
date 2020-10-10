# You want to eliminate the duplicates values in a sequence, but preserve the order of remaining items.

# if the values are hashable
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
results = list(dedupe(a))
print(results) # prints [1, 5, 2, 9, 10]


# if the values are not hashable
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 2}, {'x': 2, 'y': 1}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))
print(list(dedupe(a, key=lambda d: d['x'] + d['y'])))

# also works fine with any sequence
# with open('some_file.txt') as file_object:
#     for line in dedupe(f):
#         ...
