# You need to convert or output integers represented by binary, octal, or hexadecimal
# digits.

x = 1234
print(x, bin(x), oct(x), hex(x))

# without he 0b, 0o, or 0x prefixes
print(x, format(x, 'b'), format(x, 'o'), format(x, 'x'))

# To convert integer strings in different bases
print(int('4d2', 16))
print(int('0x4d2', 16))
print(int('10011010010', 2))
print(int('0o755', 8))
