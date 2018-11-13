import sys
import os

def main():
    v = os.getenv('PATH')
    print(v)
    # print('Python version is {}.{}.{}'.format(*v))

if __name__ == '__main__':
    main()
