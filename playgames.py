import sys
import Player
import Monty
import Pandora

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
        # Player, Monty, Pandora の生成
        player = Player.Player()
        monty = Monty.Monty()
        pandora = Pandora.Pandora()

        # 2. あなたは初めに三つの扉の中から一つの扉を選択する。
        player.select_first_answer(pandora)
        # 3. 司会者は答えを知っており，残り二つの扉の中から不正解の扉を一つ選んで開ける。
        monty.visualize_losing(pandora)

        # 4. その後、あなたは自分の選択を残りの扉に変更することが可能となる。

        # 選択肢を変更しない場合
        if pandora.is_correct():
            # この時点で正解であれば、選択変更なしの正解数を増加
            no_change_count += 1
        # Playerが選択肢を変更
        player.select_change_answer(pandora)
        if pandora.is_correct():
            # 変更後に正解であれば、選択変更ありの正解数を増加
            change_count += 1

    print(f"{count}回ゲームを施行し、")
    print(f"選択肢を変更しない場合 : {no_change_count} 回正解")
    print(f"選択肢を変更した場合   : {change_count} 回正解")
    print("しました。")

if __name__ == "__main__":
    main()