import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('line two')
    if False:
        print ('line three')
    else:
        print('Not True')

if __name__ == '__main__':
    main()
