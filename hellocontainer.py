x = (1, 2, 3, 4, 5)
y = (6, 7, 8, 9, 10)

# for i in y:
#     print(i)
z = zip(x, y)
print(x)
print(y)
print(z)

for a, b in z:
    print(f'{a} - {b}')
