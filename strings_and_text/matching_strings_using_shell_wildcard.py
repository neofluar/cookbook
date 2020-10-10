# You want to match text using the same wildcard patterns as are commonly used when
# working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))  # True
print(fnmatch('foo.txt', '?oo.txt')) # True
print(fnmatch('Data45.csv', 'Data[0-9]*'))  # True
print(fnmatch('foo.txt', '*.TXT'))  # system specific: False on Linux/Mac, True on Windows

# For system independent case matching use
print(fnmatchcase('foo.txt', '*.TXT'))  # False

# potential use with data processing
addresses = ['5412 N CLARK ST','1060 W ADDISON ST','1039 W GRANVILLE AVE',
             '5400 E CLARK ST', '2122 N CLARK ST','4802 N BROADWAY',]
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])
