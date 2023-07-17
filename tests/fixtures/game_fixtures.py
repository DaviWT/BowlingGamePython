import pytest

from src.game import Game


@pytest.fixture
def game_instance() -> Game:
    return Game()