import sys
import os
import random
import datetime

def main():
    v = list(range(25))
    print(v)
    random.shuffle(v)
    print(v)
    now = datetime.datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute)
    # print('Python version is {}.{}.{}'.format(*v))

if __name__ == '__main__':
    main()
