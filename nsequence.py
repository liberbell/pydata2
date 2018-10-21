x = (1, 'two', 3.0, [4, 'four'], 5)
y = (2, 'two', 3.0, [4, 'four'], 5)

print('x is {}'.format(x))
print(id(x[0]))
print(id(y[0]))

if x[0] is y[0]:
    print('yep')
else:
    print('nope')

if isinstance(x, tuple):
    print('yep')
else:
    print('nope')
