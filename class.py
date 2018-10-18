class Duck:
    sound = 'Quaaack'
    walking = 'walks like a line'

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('walks like a line')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__':
    main()
