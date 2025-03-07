import random
import Pandora

class Monty:
    """ゲームの司会者（Monty）クラス"""

    def visualize_losing(self, pandora: Pandora.Pandora):
        """残りの扉から、ハズレの扉を開ける。"""
        losing_list = pandora.get_remaining()
        open_door = random.choice(losing_list)
        pandora.set_open_door(open_door)