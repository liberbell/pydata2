class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._stop = 1

        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(f'expected at most 3 arguments, got {numargs}')

        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        
