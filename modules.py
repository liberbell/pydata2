import sys

def main():
    v = sys.version_info
    print('Python version is {}.{}.{}'.format(*v))

if __name__ == '__main__':
    main()
