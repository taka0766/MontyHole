import sys
from game import MontyHallGame

def main():
    """ゲームの実行と結果の表示を行うメイン関数"""
    # ゲームの施行回数をコマンドライン引数から取得（デフォルト１００万回）
    count = int(sys.argv[1]) if len(sys.argv) >= 2 else 1000000

    # 選択を変更しない場合の正解数の合計
    no_change_count = 0
    # 選択を変更した場合の正解数の合計
    change_count = 0

    # 施行回数分ゲームをループする
    for _ in range(count):
        # 選択肢を変更しない場合
        game = MontyHallGame()
        if game.play(change_choice=False):
            no_change_count += 1

        # Playerが選択肢を変更
        game = MontyHallGame()
        if game.play(change_choice=True):
            change_count += 1

    print(f"{count}回ゲームを施行し、")
    print(f"選択肢を変更しない場合 : {no_change_count} 回正解")
    print(f"選択肢を変更した場合   : {change_count} 回正解")
    print("しました。")

if __name__ == "__main__":
    main()