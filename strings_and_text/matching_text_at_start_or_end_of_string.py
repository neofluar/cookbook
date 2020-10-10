# You need to check the start or end of a string for specific text patterns, such as filename
# extensions, URL schemes, and so on.

filename = 'spam.txt'
print(filename.endswith('.txt'))

# Also startswith() and endswith() accept a tuple of possible patterns
import os
filenames = os.listdir('.')
print(filenames)
print(all(name.endswith(('.py', '.c')) for name in filenames))

# Or you can use a regexp
import re
pattern = re.compile(r'$.py')
print([re.findall(pattern, name) for name in filenames])
