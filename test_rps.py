import pytest
from rps_mod import get_score_winner
def test_get_score_winner():
    """Test get score winner"""
    get_score = get_score_winner(4, 20)
    line = 'GAME OVER'
    line += 'Player Score = 4 Computer Score = 20'
    line += 'Computer Wins the game!'
    assert get_score_winner == (line)