# You need to create or test for the floating-point values of infinity, negative infinity, or
# NaN (not a number).

a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)

import math
print(math.isinf(a), math.isnan(c))

print(a + 45, a * 10, 10 / a)
print(a / a, a + b)
print(c + 23, c / 2, math.sqrt(c))

print(float('nan') == float('nan'), float('nan') is float('nan'))
