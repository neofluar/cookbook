# You need to split a string into fields, but the delimiters (and spacing around them) aren’t
# consistent throughout the string. The built-in split() method accepts only one delimiter.

import re

line = 'asdf fjdk; afed, fjek,asdf,       foo'
words = re.split(r'[,;\s]\s*', line)
print(words)

# If capture groups are used, the matched text is also included in the result
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# to avoid that use a noncapture group
fields = re.split(r'(?:;|,|\s)\s*', line)
print(fields)
