import pytest
from door import Door

def test_door_creation():
    """ドアの作成と状態の確認"""
    door1 = Door(True)   # 当たりのドア
    door2 = Door(False)  # ハズレのドア

    assert door1.is_prize is True
    assert door2.is_prize is False
