# You’re trying to match a block of text using a regular expression, but you need the match
# to span multiple lines.

import re

comment = re.compile(r'/\*(.*?)\*/')

text_1 = '/* this is a comment */'
text_2 = '''/* this is a
              multiline comment */'''

print(comment.findall(text_1))  # prints [' this is a comment '] - OK
print(comment.findall(text_2))  # prints [] - not OK, because of . symbol

# the better solution
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text_2))  # prints [' this is a\n              multiline comment '] - OK

# in simple cases you can use a flag: re.DOTALL
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text_2))  # prints [' this is a\n              multiline comment '] - OK