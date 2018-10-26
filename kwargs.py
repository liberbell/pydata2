def main():
    x = dict(buffy= 'meow', Zilla= 'grr', Angel= 'rawr')
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('kitten {} says {}'.format(k, kwargs[k]))
        else:
            print('meow.')

if __name__ == '__main__': main()