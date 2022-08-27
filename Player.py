import random
import Pandora

class Player :
    """
    ゲームのプレイヤークラス
    """

    def __init__(self) :
        # Playerが選択した正解の値
        self.__answer = None

    def selectFirstAnswer(self, pandora:Pandora):
        """
        初回の回答を選択する。（回答可能の要素からランダムに一つ選択する。）
        """
        # Pandoraの長さ（回答の選択肢）を取得
        length = pandora.getLength()

        # 乱数から初回の選択肢を生成
        self.__answer = random.randrange(length)

        # Pandoraに回答を設定
        pandora.setPlayerAnswer(self.__answer)

    def selectChangeAnswer(self, pandora:Pandora):
        """
        Montyが開いたドアの番号を受けて、自身の回答を残りのドアに変更する。
        """
        door = pandora.getSelectableDoor()
        # Pandoraに変更した回答を設定
        self.__answer = random.choice(door)
        pandora.setPlayerAnswer(self.__answer)
