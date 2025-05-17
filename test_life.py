import pytest
from life import GameOfLife

def test_blinker():
    """Test the Blinker pattern (period 2 oscillator)."""
    game = GameOfLife(5, 5, 10)
    game.live_cells = {(2, 1), (2, 2), (2, 3)}
    expected = {(1, 2), (2, 2), (3, 2)}
    game.live_cells = game.next_gen()
    assert game.live_cells == expected
    game.live_cells = game.next_gen()
    assert game.live_cells == {(2, 1), (2, 2), (2, 3)}

def test_glider():
    """Test the Glider pattern (moves diagonally)."""
    game = GameOfLife(5, 5, 10)
    game.live_cells = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}
    # After 4 generations, glider moves down-right by 1
    for _ in range(4):
        game.live_cells = game.next_gen()
    expected = {(2, 1), (3, 2), (1, 3), (2, 3), (3, 3)}
    assert game.live_cells == expected