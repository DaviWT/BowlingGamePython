
class Game:

    def __init__(self):
        self._score = 0

    def roll(self, pins: int) -> None:
        self._score += pins

    def score(self) -> int:
        return self._score
