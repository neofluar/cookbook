# You want to round a floating-point number to a fixed number of decimal places.

print(round(1.23, 1))  # prints 1.2
print(round(-1.27, 1))  # prints -1.3
print(round(167384, -2))  # prints 167300


# ATTENTION: round rounds .5 to the closest even number
print(round(2.5, 0))  # prints 2.0
print(round(1.5, 0))  # prints 2.0

# Don't use round when you need to format output in a certain way
x = 2.5023
print(format(x, '0.2f'))  # prints 2.50
print(format(x, '0.1f'))  # prints 2.5
print(format(x, '0.0f'))  # prints 3.0 ATTENTION
