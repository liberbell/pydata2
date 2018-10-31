class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type']
        self._name = kwargs['name']
        self._sound = kwargs['sound']

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    a0 = Animal(type= 'kitten', name= 'fluffy', sound= 'rwar')
    a1 = Animal(type= 'duck', name= 'donald', sound= 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type= 'velociraptor', name= 'veronica', sound= 'hello'))

if __name__ == '__main__': main()