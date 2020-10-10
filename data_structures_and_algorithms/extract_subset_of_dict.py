# You want to make a dictionary that is a subset of another dictionary.

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}

# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

# ... and assign to 0 all others
p2 = {key: value if value > 200 else 0 for key, value in prices.items()}
print(p2)

# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p3 = {key: value for key, value in prices.items() if key in tech_names}
print(p3)
