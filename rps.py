import random
from rps_mod import get_score_winner


choices = ['rock', 'paper', 'scissors']

player_score = 0
computer_score = 0

print('Welcome to Rock, Paper, Scissors!')
print("Enter 'q' to quit. ")

while True: 

    # Prompt the user for input.
    player_input = input('\nEnter Rock, Paper, or Scissors: ').lower()

    # Break the loop if player types 'q'
    if player_input == 'q':
        break
    elif player_input not in choices:
        print('You can only choose rock, paper, or scissors. ')
        continue
        

    # Generate a random choice for computer.
    computer_choice = random.choice(choices)
    print(f'You chose {player_input}.')
    print(f'Computer chose {computer_choice}.')

    # Compare player input with computer selection.
    if player_input == computer_choice:
        print('Draw!')

    elif (player_input == 'rock' and computer_choice == 'scissors') or \
         (player_input == 'paper' and computer_choice == 'rock') or \
         (player_input == 'scissors' and computer_choice == 'paper'):
        print('Player wins!')
        player_score += 1

    else:
        print('Computer wins!')
        computer_score += 1

# Get the score and game status.
get_score_winner(player_score, computer_score)




    










