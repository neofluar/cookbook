# You want to  look for the shortest possible match in a string.

import re

str_pat = re.compile(r'\"(.*)\"')
text_1 = 'Computer says "No."'
print(str_pat.findall(text_1))  # prints ['No.'] - ok

text_2 = 'Computer says "No." Phone says "yes."'
print(str_pat.findall(text_2))  # prints ['No." Phone says "yes.'] - Not ok

better_pat = re.compile(r'\"(.*?)\"')
print(better_pat.findall(text_2))  # prints ['No.', 'yes.'] - Ok
