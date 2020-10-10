# You want to match or search text for a specific pattern.

text = 'yeah, but no, but yeah, but no, but yeah'

# Search for the location of the first occurrence
print(text.find('no'))  # prints 10

# For more complicated matching, use regular expressions and the re module
import re

text1 = '11/27/2012'
text2 = "Mov 27, 2012"

datepat = re.compile(r'\d+/\d+/\d+')  # better to precompile pattern for reuse

# match finds the first match
print(datepat.match(text1)[0])  # prints '11/27/2012'

# for all existing matches use findall()
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))  # prints ['11/27/2012', '3/13/2013']

# grouping
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0), m.group(1), m.group(2), m.group(3), m.groups(), sep='---')

# to find matches iteratively use finditer()
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
for m in datepat.finditer(text):
    print(m.groups())
