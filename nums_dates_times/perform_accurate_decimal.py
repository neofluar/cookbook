# You need to perform accurate calculations with decimal numbers, and don’t want the
# small errors that naturally occur with floats.

a, b = 4.2, 2.1
print(a + b)  # prints 6.300000000000001

from decimal import Decimal

a, b = Decimal('4.2'), Decimal('2.1')
print(a + b)  # prints 6.3 as expected

# Local calculation context
print(1.3 / 1.7)  # prints 0.7647058823529412

from decimal import localcontext

a, b = Decimal('1.3'), Decimal('1.7')
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)  # prints 0.765 as expected

# another weird example
nums = [1.23e28, 1, -1.23e28]
print(sum(nums))  # prints 0.0 as though 1 disappeared

import math

print(math.fsum(nums))  # prints 1.0 as expected
