import random

def random_number():
    counter = 0
    my_random_number = random.randint(1, 100)
    number = int(input('Guess a number between 1 and 100: '))
    while 1 <= number <= 100:
        if number > my_random_number:
            print()
            print('Too high, try again')
            counter += 1
            number = int(input('Guess again? '))
        elif number < my_random_number:
            print()
            print('Too low, try again')
            counter += 1
            number = int(input('Guess again? '))
        elif number == my_random_number:
            print()
            print('Congratulations! You got the correct number after', counter, 'guesses')
            counter = 0
            my_random_number = random.randint(1, 100)
            number = int(input('Play again! Guess a number between 1 and 100: '))

random_number()
