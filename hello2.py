# print('Hello World.')

def f1(f):
    def f2():
        print('this is before function call')
    return f2

def f3():
    print('this is f3')

x = f1()
x()