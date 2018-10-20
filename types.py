a = 8
b = 'abc'

x = 'seven {} {}'.format(8, 'abc')
y = f'seven {a:<09} {b:>09}'

print('x is {}'.format(x))
print('y is {}'.format(y))
print(type(x))
print(type(y))
