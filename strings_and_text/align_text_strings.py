# You need to format text with some sort of alignment applied.

text = 'Hello World'

# using r-, ljust and center() methods
print(text.ljust(20))   # prints 'Hello World         '
print(text.rjust(20))   # prints '         Hello World'
print(text.center(20))  # prints '    Hello World     '

print(text.rjust(20,'='))   # prints '=========Hello World'
print(text.center(20,'*'))  # prints '****Hello World*****'


# using the format() function
print(format(text, '<20'))   # prints 'Hello World         '
print(format(text, '>20'))   # prints '         Hello World'
print(format(text, '*^20'))  # prints '****Hello World*****'

print('{:>10s} {:>10s}'.format('Hello', 'World'))  # prints '     Hello      World'

x = 1.2345
print(format(x, '^20.2f'))  # prints '        1.23        '
