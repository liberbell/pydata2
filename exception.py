def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    if numargs < 1:
        raise TypeError(f'excepted at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
