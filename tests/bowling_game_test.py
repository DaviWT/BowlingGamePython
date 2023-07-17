from src.game import Game


def test_worst_scenario_game(game_instance: Game) -> None:
    # Act
    for _ in range(20):
        game_instance.roll(0)
    game_score = game_instance.score()

    # Assert
    assert game_score == 0


def test_average_scenario_game(game_instance: Game) -> None:
    # Act
    for _ in range(20):
        game_instance.roll(4)
    game_score = game_instance.score()

    # Assert
    assert game_score == 80


def test_single_spare(game_instance: Game) -> None:
    # Act
    game_instance.roll(2)
    game_instance.roll(4)
    game_instance.roll(5)
    game_instance.roll(5)
    game_instance.roll(3)

    for _ in range(15):
        game_instance.roll(0)
    game_score = game_instance.score()

    # Assert
    assert game_score == 22

def test_single_strike(game_instance: Game) -> None:
    # Act
    game_instance.roll(2)
    game_instance.roll(4)
    game_instance.roll(10)
    game_instance.roll(5)
    game_instance.roll(3)

    for _ in range(14):
        game_instance.roll(0)
    game_score = game_instance.score()

    # Assert
    assert game_score == 32

def test_sequential_spare(game_instance: Game) -> None:
    # Act
    game_instance.roll(2)
    game_instance.roll(4)
    game_instance.roll(5)
    game_instance.roll(5)
    game_instance.roll(5)
    game_instance.roll(5)
    game_instance.roll(3)

    for _ in range(13):
        game_instance.roll(0)
    game_score = game_instance.score()

    # Assert
    assert game_score == 37

def test_sequential_strike(game_instance: Game) -> None:
    # Act
    game_instance.roll(2)
    game_instance.roll(4)
    game_instance.roll(10)
    game_instance.roll(10)
    game_instance.roll(5)
    game_instance.roll(3)

    for _ in range(12):
        game_instance.roll(0)
    game_score = game_instance.score()

    # Assert
    assert game_score == 52
