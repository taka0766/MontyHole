import pytest
from door import Door
from host import Host

def test_host_open_goat_door():
    """ホストが適切なハズレのドアを開けるか確認"""
    doors = [Door(False), Door(True), Door(False)]
    host = Host(doors)

    chosen_door = 1  # プレイヤーが当たりのドアを選んだ場合
    open_door = host.open_goat_door(chosen_door)

    assert open_door != chosen_door  # 選択したドア以外を開けること
    assert doors[open_door].is_prize is False  # ハズレのドアを開けること
