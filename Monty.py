import random
import Pandora

class Monty :
    """
    ゲームの司会者（Monty）クラス
    """
    def __init__(self):
        pass

    def visualizeLosing(self, pandora:Pandora):
        """
        残りの扉から、ハズレの扉を開ける。
        """
        losing_list = pandora.getRemaining()
        open_door = random.choice(losing_list)
        pandora.setOpenDoor(open_door)
