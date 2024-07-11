# Rock Paper Scissors
 A simple command-line implementation of the classic Rock, Paper, Scissors game.

Files:

rps.py : 

This script implements the main game logic for a command-line Rock, Paper, Scissors game. Players can input their choice of 'rock', 'paper', or 'scissors', and the computer randomly selects its choice. The game tracks the scores of both the player and the computer, and players can quit the game at any time by entering 'q'. At the end of the game, the scores and the winner are displayed using the get_score_winner function from the rps_mod module.

rps_mod.py :

This module defines the get_score_winner function, which prints the final scores of the player and the computer and determines the winner of the Rock, Paper, Scissors game. The function handles three possible outcomes: player wins, computer wins, or a draw.

test_rps.py :

This script contains unit tests for the Rock, Paper, Scissors game, specifically testing the get_score_winner function from the rps_mod module. The tests are written using the pytest framework to ensure that the scoring and game outcome logic works correctly.