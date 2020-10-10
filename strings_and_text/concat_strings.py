# You want to combine many small strings together into a larger string.
# Try to avoid str + str

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(''.join(parts))

together = 'Hello'    'World'
print(together)

# using a generator
def samples():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ''.join(samples())
print(text)

# A hybrid scheme that’s smart about combining I/O operations
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(samples(), 32768):
    file_object.write(part)

