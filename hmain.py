import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('line two')
    print ('line three')

if __name__ == '__main__':
    main()
