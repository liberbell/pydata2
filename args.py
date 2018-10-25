def main():
    kitten('meow', 'grrr', 'purr', 'Hello', 'World', 'Wow')

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')
        # other pattern

if __name__ == '__main__': main()
