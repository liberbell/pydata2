from decimal import *

x = 7 * 3.14159
y = .1 + .1 + .1 - .3

a = Decimal('.10')
b = Decimal('.30')
c = a + a + a - b

print('x is {}'.format(x))
print('y is {}'.format(y))
print('z is {}'.format(c))
print(type(x))
print(type(y))
print(type(c))
