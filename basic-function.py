def main():
    x = 5
    y = x
    y = 3
    print(id(x))
    print(id(y))
    # kitten(x)
    # print(f'in a main: x is {x}')
    # print(x)

def kitten(a):
    print(a)
    print(id(a))
    a = 3
    print(id(a))
    print('Meow.')
    print(a)
    # return 'Meow.'

if __name__ == '__main__':
    main()
