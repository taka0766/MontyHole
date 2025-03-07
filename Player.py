import random
from typing import List
from Door import Door

class Player:
    """プレイヤーのクラス"""

    def choose_door(self, num_doors: int) -> int:
        """扉を選択する"""
        return random.randrange(num_doors)

    def change_door(self, doors: List[Door], current_choice: int) -> int:
        """扉の選択を変更する"""
        available_doors = [
            i for i, door in enumerate(doors) if i != current_choice and not door.is_open
        ]
        return random.choice(available_doors)