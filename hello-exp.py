def main():
    try:
        x = int('foo')
    except ValueError:
        print('I caught a ValueError {}'.format)

if __name__ == '__main__':
    main()
