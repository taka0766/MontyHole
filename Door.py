class Door:
    """扉の状態を管理するクラス"""

    def __init__(self, is_prize: bool = False):
        """扉の初期化"""
        self.is_prize = is_prize
        self.is_open = False

    def open(self):
        """扉を開ける"""
        self.is_open = True

    def __repr__(self):
        """扉の状態を文字列で表現"""
        return f"Door(prize={self.is_prize}, open={self.is_open})"