def main():
    x = 5
    kitten(x)
    print(f'in a main: x is {x}')
    # print(x)

def kitten(a):
    print(a)
    a = 3
    print('Meow.')
    print(a)
    # return 'Meow.'

if __name__ == '__main__':
    main()
