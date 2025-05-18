# MontyHole / モンティ・ホール問題シミュレーター

A Python simulation that demonstrates the famous Monty Hall problem, where switching your choice statistically improves your chances of winning.

有名な「モンティ・ホール問題」をPythonでシミュレートし、「選択を変える方が当たる確率が高い」という直感に反する結果を実証します。

---

## 📌 Overview / 概要

The Monty Hall problem is a probability puzzle based on a game show scenario.  
This simulator lets you test two strategies:  
- **Stay with your first choice**
- **Switch after the host opens a door**

モンティ・ホール問題とは、3つのドアのうち1つに当たりがあり、プレイヤーが1つ選んだ後にホストが外れのドアを1つ開け、「選択を変えるかどうか」を問う確率パズルです。  
本プログラムでは「変更する／変更しない」両方の戦略を繰り返し実行して、勝率の違いを比較します。

---

## 🧠 What is the Paradox? / この問題のパラドックスとは？

Many people believe that after one losing door is revealed, the odds of winning become 50/50 between the remaining two doors.  
However, **switching doors actually gives you a 2/3 chance of winning**, while staying keeps you at only 1/3.

この問題は「残り2つなら半々のはず」と考えたくなる直感に反し、**ドアを変えた方が当たる確率が高い（2/3）**という逆説的な結果を示します。  
このシミュレーションで、数値としてそれを確認できます。

---

## 🧩 Logic Overview / ソースコードのロジック

### 🔹 クラス構成（OOPベース）

| ファイル名       | 説明 |
|----------------|------|
| `Door.py`      | ドアオブジェクト（当たり／外れの状態を持つ） |
| `Host.py`      | ホストの行動ロジック（外れのドアを開ける） |
| `Player.py`    | プレイヤーの選択行動（変更 or 維持）         |
| `Game.py`      | ゲームの全体進行（1回分の試行）              |
| `playgames.py` | 複数回試行して統計をとるメインスクリプト     |

### 🔹 プレイの流れ

1. 3枚のドアのうち1枚に当たり（景品）を配置
2. プレイヤーが1枚選ぶ
3. ホストが外れのドアを1枚開ける
4. プレイヤーが変更するか決める
5. 当たりかどうかを判定

---

## 🧪 Example Output / 実行例

```bash
1000000回ゲームを施行し、
選択肢を変更しない場合 :  332344 回正解
選択肢を変更した場合   : 667656 回正解
しました。

````

---

## ▶️ How to Run / 実行方法

1. Clone the repository / リポジトリをクローン：

```bash
git clone https://github.com/taka0766/MontyHole.git
cd MontyHole
```

2. Run the simulation / シミュレーションを実行：

```bash
python playgames.py
```

3. The number of game simulations can be specified as an argument in playgames.py (default: 1,000,000 times).
 / ゲームの試行回数は `playgames.py` の引数から取得できます（デフォルト１００万回）。

---

## ⚙️ Requirements / 必要な環境

* Python 3.x（標準ライブラリのみ使用）

---

## 📁 File Structure / ファイル構成

```
MontyHole/
├── Door.py         # ドアオブジェクトの定義
├── Game.py         # 1回のモンティ・ホールゲームを管理
├── Host.py         # ホストの行動定義
├── Player.py       # プレイヤーの選択定義
├── playgames.py    # 複数回のシミュレーション実行スクリプト
└── README.md       # 本ドキュメント
```

---

## 📝 License / ライセンス

License not specified. Contact the author for usage or redistribution.
ライセンスは未指定です。利用や再配布については作成者にお問い合わせください。

---

## 🙋 Author / 作者

Created by [taka0766](https://github.com/taka0766)
このプログラムは [taka0766](https://github.com/taka0766) によって作成されました。
