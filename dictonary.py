def main():
    animals = {'kitten': 'meow', 'puppy': 'ruff', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
    # for k, v in animals.items():
    #     print(f'{k}: {v}')
    for k in animals.keys():
        print(k)
    # print_dict(animals)

def print_dict(o):
    for k, v in o.items():
        print(f'{k}: {v}')
    # for x in o:
    #     print(f'{x}: {o[x]}')

if __name__ == '__main__': main()