def get_score_winner(player_score, computer_score):
    """Provide the score and winner at the end of game."""
    print ('\nGAME OVER!')
    print (f'Player Score = {player_score} Computer Score = {computer_score}')
    if player_score > computer_score:
        print('Player wins the game!')

    elif player_score == computer_score:
        print('DRAW!')

    else:
        print('Computer Wins the game!')