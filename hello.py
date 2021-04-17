import sys

print(sys.executable)

import json

a = {'b': 3, 'c': {'d': 4}}
with open('test.json', 'w') as f:
    json.dump(a, f)
