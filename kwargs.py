def main():
    kitten(buffy= 'meow', Zilla= 'grr', Angel= 'rawr')

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('kitten {} says ')