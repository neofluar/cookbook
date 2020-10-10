# You need to search for and possibly replace text in a case-insensitive manner

import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 's-n-a-k-e', text, flags=re.IGNORECASE))

# make replacing text match the case of the matched text
def match_case(word):

    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace

print(re.sub('python', match_case(word='snake'), text, flags=re.IGNORECASE))
