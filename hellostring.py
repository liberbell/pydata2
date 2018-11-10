class bunny:
    def __init__(self, n):
        self._n = n
    def __rper__(self):
        return f'the number of bunnies is {self._n}'

s = 'Hello World.'
print(repr(s))
