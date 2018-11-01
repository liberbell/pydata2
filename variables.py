class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rwar'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    a0 = Animal(type= 'kitten', name= 'fluffy', sound= 'rwar')
    a1 = Animal(type= 'duck', name= 'donald', sound= 'quack')
    print(a0)
    print(a1)
    a0.name('Joe!')
    print(a1._name)
 
    # print_animal(a0)
    # print_animal(a1)
    # print_animal(Animal(type= 'velociraptor', name= 'veronica', sound= 'hello'))
    # print_animal(Animal())

if __name__ == '__main__': main()