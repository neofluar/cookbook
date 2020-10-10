# You want to perform various calculations (min, max, sorting, etc.) on a dictionary of data.

prices = {'ZZPL': 612.78,'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 31.20, 'FB': 10.75}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price) # prints (10.75, 'FB')

max_price = max(zip(prices.values(), prices.keys()))
print(max_price) # prints (612.78, 'ZZPL')

sorted_prices = sorted(zip(prices.values(), prices.keys()))
print(sorted_prices) # in the case of duplicate values they are sorted by next item (key)


# zip() makes an iterator that can only be consumed only once
names_and_prices = zip(prices.values(), prices.keys())
print(min(names_and_prices)) # prints (10.75, 'FB')
try:
    print(max(names_and_prices))
except ValueError:
    print('ERROR: names_and_prices are empty sequence')


# Using a key function
print(min(prices, key=lambda k: prices[k])) # prints 'FB'
