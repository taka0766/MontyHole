import sys
import Player
import Monty
import Pandora

# ゲームの施行回数をコマンドライン引数から取得（デフォルト１００万回）
args = sys.argv
count = int(args[1]) if (len(args) >= 2) else 1000000

# 選択を変更しない場合の正解数の合計
no_change = 0
# 選択を変更した場合の正解数の合計
change = 0

# 施行回数分ゲームをループする
for num in range(count):
    # Player,Monty,Pandoraの生成
    player = Player.Player()
    monty = Monty.Monty()
    pandora = Pandora.Pandora()

    # 2. あなたは初めに三つの扉の中から一つの扉を選択する。
    player.selectFirstAnswer(pandora)
    # 3. 司会者は答えを知っており，残り二つの扉の中から不正解の扉を一つ選んで開ける。
    monty.visualizeLosing(pandora)

    # 4. その後、あなたは自分の選択を残りの扉に変更することが可能となる。

    # 選択肢を変更しない場合
    if pandora.isCorrect():
        # この時点で正解であれば、選択変更なしの正解数を増加
        no_change+=1
    # Playerが選択肢を変更
    player.selectChangeAnswer(pandora)
    if pandora.isCorrect():
        # 変更後に正解であれば、選択変更ありの正解数を増加
        change+=1

print(str(count) + "回ゲームを施行し、")
print("選択肢を変更しない場合 : " + str(no_change) + " 回正解")
print("選択肢を変更した場合   : " + str(change) + " 回正解")
print("しました。")
