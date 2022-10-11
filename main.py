import random

while True:
    def game():
        choices = ['rock', 'paper', 'scissors']

        computer = random.choice(choices)

        name = input('Rock, Paper, or Scissors? ').lower()
        if name in choices:
            print(computer)
        else:
            print('Please make a valid move')
            game()

        if name == 'scissors' and computer == 'paper':
            print('You won! Scissors beats paper')
        elif name == 'paper' and computer == 'scissors':
            print('You lost! Paper loses to Scissors')
        elif name == 'paper' and computer == 'rock':
            print('You won! Paper beats Rock')
        elif name == 'rock' and computer == 'paper':
            print('You lost! Rock loses to Paper')
        elif name == 'rock' and computer == 'scissors':
            print('You won! Rock beats Scissors')
        elif name == 'scissors' and computer == 'rock':
            print('You lost! Scissors loses to Rock')
        elif name == computer:
            print('tie!')
            game()

    game()

    play_again = input("play again? (Y/N)").lower()

    if play_again != 'y':
        break
print('thanks for playing')
