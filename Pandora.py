import random

class Pandora:
    """
    複数の扉の情報を管理するクラス
    """

    def __init__(self, length:int=3):
        # 回答可能なドアの総数
        self.__door = list(range(length))
        # 今回の正解のドアの番号をランダムに生成
        self.__answer = random.randrange(length)

        self.__player_answer = None

    def getLength(self):
        """
        回答可能なドアの総数を返す。
        """
        return len(self.__door)

    def setPlayerAnswer(self, answer):
        """
        Playerが選択した回答を設定
        """
        self.__player_answer = answer

    def getRemaining(self):
        """
        選択されていないドアの中で、ハズレであるドアの添字をリストで返す
        """
        tmp_door = self.__door.copy()
        # Playerが選択したドアを除外する
        tmp_door.remove(self.__player_answer)
        # 残りのドアに回答のドアが存在する場合は、除外する
        if self.__answer in tmp_door:
            tmp_door.remove(self.__answer)

        return tmp_door

    def setOpenDoor(self, open_door:int):
        """
        ハズレのドアを開く
        """
        if self.__answer == open_door:
            raise ValueError("正解の扉を開くことはできません")
        if self.__player_answer == open_door:
            raise ValueError("Playerが選択した扉を開くことはできません")
        self.__open_door = open_door

    def getSelectableDoor(self):
        """
        選択可能なドアを返す。
        """
        # 回答可能な全てのドアを取得する。
        tmp_door = self.__door.copy()
        # すでにPlayerが選択したものを除外
        tmp_door.remove(self.__player_answer)
        # すでに開けられているドアを除外
        tmp_door.remove(self.__open_door)
        return tmp_door

    def isCorrect(self):
        """
        Playerの選択が正解か否かを判定する
        """
        return self.__answer == self.__player_answer
