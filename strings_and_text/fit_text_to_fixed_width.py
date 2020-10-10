# You have long strings that you want to reformat so that they fill a user-specified number
# of columns.

long_str = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap

print(textwrap.fill(long_str, 40))
print(textwrap.fill(long_str, 40, initial_indent='++++'))
print(textwrap.fill(long_str, 40, subsequent_indent='++++'))
