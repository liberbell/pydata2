def main():
    for i in inclusive_range(25):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    stop = 1

    if numargs < 1:
        raise TypeError(f'expected at lease 1 argement, got {numargs}')
    elif numargs == 1:
        