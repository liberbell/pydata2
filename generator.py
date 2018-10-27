def main():
    for i in inclusive_range(1, 25):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    if numargs < 1:
        raise TypeError(f'expected at lease 1 argement, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 argements, got {numargs}')
    
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__': main()