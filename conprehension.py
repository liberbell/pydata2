def main():
    seq = range(100)
    # seq2 = [x for x in seq if x % 3 != 0]
    from math import pi
    # seq2 = [(x, x**2) for x in seq]
    # seq2 = [round(pi, i) for i in seq]
    seq2 = { x: x**2 for x in seq}
    print_list(seq)
    print(seq2)

def print_list(o):
    for x in o:
        print(x, end = ' ')
    print()

if __name__ == '__main__': main()