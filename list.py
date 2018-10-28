def main():
    game = ['rock', 'paper', 'scissor', 'lizard', 'spock']
    print(game[1])
    print_list(game)

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()

if __name__ == '__main__' : main()