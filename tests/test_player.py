import pytest
from player import Player

def test_player_strategy():
    """プレイヤーの戦略が正しく設定されているか"""
    player1 = Player(True)  # 変更する戦略
    player2 = Player(False)  # 変更しない戦略

    assert player1.switch_strategy is True
    assert player2.switch_strategy is False
