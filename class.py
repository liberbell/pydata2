class Duck:
    sound = 'Quaaack'
    walking = 'walking like a line'

    def quack(self):
        # print('Quaaack!')
        print(self.sound)

    def walk(self):
        # print('walks like a line')
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__':
    main()
