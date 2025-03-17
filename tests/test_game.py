import pytest
from game import MontyHallGame

def test_game_simulation_change():
    """ドアを変更する場合の勝率が理論値に近いか"""
    game = MontyHallGame()
    win_count = 0
    num_trials = 1000  # シミュレーション回数

    for _ in range(num_trials):
        if game.play(change_choice=True):  # ドアを変更する
            win_count += 1

    win_rate = win_count / num_trials
    expected_win_rate = 2 / 3  # 理論上の勝率

    # 許容範囲内で期待値と比較
    assert abs(win_rate - expected_win_rate) < 0.05, f"Win rate {win_rate} differs from expected {expected_win_rate} when changing doors"

def test_game_simulation_no_change():
    """ドアを変更しない場合の勝率が理論値に近いか"""
    game = MontyHallGame()
    win_count = 0
    num_trials = 1000  # シミュレーション回数

    for _ in range(num_trials):
        if game.play(change_choice=False):  # ドアを変更しない
            win_count += 1

    win_rate = win_count / num_trials
    expected_win_rate = 1 / 3  # 理論上の勝率

    # 許容範囲内で期待値と比較
    assert abs(win_rate - expected_win_rate) < 0.05, f"Win rate {win_rate} differs from expected {expected_win_rate} when not changing doors"
