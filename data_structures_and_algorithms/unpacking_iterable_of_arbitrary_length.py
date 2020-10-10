# You need to unpack N elements from an iterable, but the iterable may be longer than N elements,
# causing a “too many values to unpack” exception. Solution: Python “star expressions”.

def drop_first_last(grades):
    _, *middle, _ = grades
    return sum(middle)/len(middle)

avg_middle = drop_first_last([1, 4, 2, 3, 4])
print(avg_middle)


user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
assert isinstance(phone_numbers, list)  # always list!
print(phone_numbers)


*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
assert isinstance(trailing, list)
print(trailing)


a, b, c, *rest = 'abcdefghi'
assert isinstance(rest, list)
print(rest)


records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4),]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar',s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(homedir)


record = ('ACME', 50, 123.45, (12, 18, 2012))
name2, *_, (*_, year2) = record
print(year2)
