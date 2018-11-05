class Myclass(str):
    def __str__(self):
        return self[::-1]

s = 'Hello World.'
print(s)
