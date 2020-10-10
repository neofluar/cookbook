# You have a sequence, and you'd like to determine the most frequently occuring items

words = ['foo', 'pak', 'mir', 'foo', 'foo',
         'bar', 'bar', 'buz', 'mir', 'pak',
         'foo', 'buz', 'pec', 'pec', 'pec']

from collections import Counter

word_counts = Counter(words) # it's a dict under the covers
print(word_counts)

top_three = word_counts.most_common(3)
print(top_three)
print(word_counts['bar']) # prints 2

# To add more words
morewords = ['pec', 'pik', 'mir']
for word in morewords:
    word_counts[word] += 1
print(word_counts['pec']) # prints 4

# or alternatively
word_counts.update(morewords)
print(word_counts['pik']) # prints 2


# Counters can be easily combined using +/-
a = Counter(words)
b = Counter(morewords)

print(a + b)
print(a - b) # prints Counter({'foo': 4, 'pak': 2, 'bar': 2, 'buz': 2, 'pec': 2, 'mir': 1})
print(b - a) # prints Counter({'pik': 1})
