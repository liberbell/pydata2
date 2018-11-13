import sys
import os
import random

def main():
    v = list(range(25))
    print(v)
    random.shuffle(v)
    print(v)
    # print('Python version is {}.{}.{}'.format(*v))

if __name__ == '__main__':
    main()
