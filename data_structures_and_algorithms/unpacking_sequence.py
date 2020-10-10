# You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

p = (4, 5)
x, y = p
print(x, y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data
print(year)

s = 'Hello'
a, b, c, d, e = s
print(a)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares1, price1, _ = data
print(price1)
