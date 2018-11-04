def main():
    try:
        x = 5/0
    except ValueError:
        print('I caught a ValueError {}'.format)

if __name__ == '__main__':
    main()
