import random
from typing import List
from door import Door

class Host:
    """司会者のクラス"""

    def open_losing_door(self, doors: List[Door], player_choice: int) -> int:
        """プレイヤーが選択していない不正解の扉を開ける"""
        losing_doors = [
            i
            for i, door in enumerate(doors)
            if not door.is_prize and i != player_choice and not door.is_open
        ]
        if not losing_doors:
          raise ValueError('開けることのできるドアがありません')

        open_door_index = random.choice(losing_doors)
        doors[open_door_index].open()
        return open_door_index