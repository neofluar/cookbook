# You want to clean up an unreadable mess of hardcoded slice indices

######   '0123456789012345678901234567890123456789012345678901234567890'
record = '....................100           ......513.25     ..........'
cost1 = int(record[20:32]) * float(record[40:48]) # unreadable

SHARES = slice(20, 32)
PRICE = slice(40, 48)
cost2 = int(record[SHARES]) * float(record[PRICE]) # much better
assert cost1 == cost2


a = slice(5, 50, 2)
print(a.start, a.stop, a.step) # prints 5, 50, 2

s = 'HelloWorld'
mapped_slice = a.indices(len(s)) # maps into a sequence of a specific size
print(mapped_slice) # prints (5, 10, 2)
for i in range(*mapped_slice):
    print(s[i]) # prints W r d
