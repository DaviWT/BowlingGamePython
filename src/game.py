from typing import List

from src.roll import Roll


class Game:

    def __init__(self):
        self._roll_list: List[Roll] = []

    def roll(self, pins: int) -> None:
        self._roll_list.append(Roll(pins))
        if pins == 10:
            self._roll_list.append(Roll(0))

    def score(self) -> int:
        final_score = 0
        for roll_index in range(0, len(self._roll_list), 2):
            first_roll = self._roll_list[roll_index].pins
            second_roll = self._roll_list[roll_index + 1].pins
            frame_score = first_roll + second_roll
            final_score += frame_score
            if first_roll == 10:
                first_next_result = self._roll_list[roll_index + 2].pins
                second_next_result = self._roll_list[roll_index + 3].pins
                final_score += first_next_result + second_next_result
            elif first_roll + second_roll == 10:
                first_next_result = self._roll_list[roll_index + 2].pins
                final_score += first_next_result

        return final_score
