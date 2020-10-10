# You have entered a time machine and suddenly find yourself working on elementary-
# level homework problems involving fractions. Or perhaps you’re writing code to make
# calculations involving measurements made in your wood shop.

from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)
c = a * b
print(a + b, a * b, c)

# Getting numerator/denominator
print(a.numerator, b.denominator)

# Converting to a float
print(float(b))

# Limiting the denominator of a value
print(c.limit_denominator(), c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
print(Fraction(*x.as_integer_ratio()))
