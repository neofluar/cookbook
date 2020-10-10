# You’re working with Unicode strings, but need to make sure that all of the strings have
# the same underlying representation.

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1, '<>', s2)
print(s1 == s2)  # WHOA it's False!

import unicodedata

t1 = unicodedata.normalize('NFC', s1)  # NFC means fully composed
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)  # Now that's nice
print(ascii(t1))  # prints 'Spicy Jalape\xf1o'

t3 = unicodedata.normalize('NFD', s1)  # NFD means fully decomposed
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)  # Now that's nice
print(ascii(t3))  # prints 'Spicy Jalapen\u0303o'
