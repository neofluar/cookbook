# You want to search for and replace a text pattern in a string.

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

# rewrite dates of the another form 11/27/2012 -> 27.11.2012
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\2.\1.\3', text))

# precompile the pattern in the case of reuse later
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\2.\1.\3', text))

# a substitution callback function
from calendar import month_abbr

def change_date(m):
    m_abbr = month_abbr[int(m.group(1))]
    return f'{m.group(2)} {m_abbr} {m.group(3)}'

print(datepat.sub(change_date, text))

# how many substitutions were made
newtext, n = datepat.subn(r'\2.\1.\3', text)
print(n)
