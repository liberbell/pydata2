def main():
    x = ('meow', 'grrr', 'purr', 'Hello', 'World', 'Wow')
    kitten(*x)

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')
 
if __name__ == '__main__': main()
