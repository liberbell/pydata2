import sys

def main():
    try:
        x = 5/0
    except ValueError:
        print('I caught a ValueError {}'.format)
    except:
        print(f'unknown error: {sys.exc_info()}')
    else:
        print('good job')
        print(x)

if __name__ == '__main__':
    main()
