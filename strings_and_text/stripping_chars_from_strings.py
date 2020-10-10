# You want to strip unwanted characters, such as whitespace, from the beginning, end, or
# middle of a text string.

# Whitespace stripping
s = '      hello world    \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.rstrip('='))

# For inner string space use replace()...
print(s.replace(' ', ''))

# ...or a regexp
import re
print(re.sub('\s+', ' ', s))
