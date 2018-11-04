def main():
    try:
        x = 5/3
    except ValueError:
        print('I caught a ValueError {}'.format)
    except ZeroDivisionError:
        print('dont divide by zero')
    else:
        print('good job')
        print(x)

if __name__ == '__main__':
    main()
