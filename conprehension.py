def main():
    seq = range(11)
    # seq2 = [x for x in seq if x % 3 != 0]
    from math import pi
    # seq2 = [(x, x**2) for x in seq]
    # seq2 = [round(pi, i) for i in seq]
    seq2 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o:
        print(x, end = ' ')
    print()

if __name__ == '__main__': main()