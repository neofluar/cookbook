# You need to format a number for output, controlling the number of digits, alignment,
# inclusion of a thousands separator, and other details.

x = 1234.56789

# Two decimal places of accuracy
print(format(x, '0.2f'))

# Right justified in 10 chars, one-digit accuracy
print(format(x, '<10.1f'))  # prints '1234.6    '

# Centered
print(format(x, '^10.1f'))

# E notation
print(format(x, '.2e'))

# Inclusion of thousands separator
print(format(x, ',.2f'))

# Formatting of values with a thousands separator is not locale aware
swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators))  # prints 1.234,56789
