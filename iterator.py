class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._stop = 1

        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')
