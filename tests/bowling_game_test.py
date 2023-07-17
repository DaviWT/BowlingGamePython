from src.game import Game


def test_worst_game() -> None:
    # Arrange
    game = Game()

    # Act
    for _ in range(20):
        game.roll(0)
    game_score = game.score()

    # Assert
    assert game_score == 0
