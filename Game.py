import random
from typing import List
from Door import Door
from Player import Player
from Host import Host

class MontyHallGame:
    """モンティ・ホールゲームの進行を管理するクラス"""

    def __init__(self, num_doors: int = 3):
        """ゲームの初期化"""
        self.num_doors = num_doors
        self.doors = self._create_doors()
        self.player = Player()
        self.host = Host()

    def _create_doors(self) -> List[Door]:
        """扉を作成する"""
        prize_door = random.randrange(self.num_doors)
        return [Door(is_prize=(i == prize_door)) for i in range(self.num_doors)]

    def play(self, change_choice: bool) -> bool:
        """ゲームをプレイする"""
        player_choice = self.player.choose_door(self.num_doors)
        self.host.open_losing_door(self.doors, player_choice)

        if change_choice:
            player_choice = self.player.change_door(self.doors, player_choice)

        return self.doors[player_choice].is_prize