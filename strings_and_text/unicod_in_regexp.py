# You are using regular expressions to process text, but are concerned about the handling
# of Unicode characters.

import re

num = re.compile('\d+')
print(num.findall('123'))
print(num.findall('\u0661\u0662\u0663'))  # there are rudimentary knowledge of certain Unicode already

# try to normalize and sanitize input before
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))  # match!
print(pat.match(s.upper()))  # Doesn't match
print(s.upper())  # prints 'STRASSE'
