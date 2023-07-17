from src.game import Game


def test_worst_game(game_instance: Game) -> None:
    # Act
    for _ in range(20):
        game_instance.roll(0)
    game_score = game_instance.score()

    # Assert
    assert game_score == 0


def test_all_ones_game(game_instance: Game) -> None:
    # Act
    for _ in range(20):
        game_instance.roll(1)
    game_score = game_instance.score()

    # Assert
    assert game_score == 20
