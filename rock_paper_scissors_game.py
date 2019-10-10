import random

def game():
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        choice = 'rock'
    if computer_choice == 2:
        choice = 'paper'
    if computer_choice == 3:
        choice = 'scissors'
    user_choice = int(input("Enter your choice (1 for 'rock', 2 for 'paper', 3 for 'scissors'): "))
    print('The computer selected', choice)
    if user_choice == 1:
        your_choice = 'rock'
        print('The user selected', your_choice)
        if computer_choice == 1:
            print('Play again to determine the winner!')
        elif computer_choice == 2:
            print('The computer wins. Paper wraps rock.')
        elif computer_choice == 3:
            print('The user wins. Rock smashes scissors.')
    elif user_choice == 2:
        your_choice = 'paper'
        print('The user selected', your_choice)
        if computer_choice == 1:
            print('The user wins. Paper wraps rock.')
        elif computer_choice == 2:
            print('Play again to determine the winner!')
        elif computer_choice == 3:
            print('The computer wins. Scissors cuts paper.')
    elif user_choice == 3:
        your_choice = 'scissors'
        print('The user selected', your_choice)
        if computer_choice == 1:
            print('The computer wins. Rock smashes scissors.')
        elif computer_choice == 2:
            print('The user wins. Scissors cuts paper.')
        elif computer_choice == 3:
            print('Play again to determine the winner!')

game()
