#!/usr/bin/env python3
"""
クイズゲーム (Quiz Game)

2問連続で正解するとクリアとなる算数クイズゲームです。
"""

import random
from calculator import add, subtract, multiply


def generate_quiz():
    """ランダムな算数クイズ問題を生成する"""
    # 演算の種類を選択
    operations = [
        {'name': '加算', 'symbol': '+', 'func': add},
        {'name': '減算', 'symbol': '-', 'func': subtract},
        {'name': '乗算', 'symbol': '*', 'func': multiply}
    ]

    operation = random.choice(operations)

    # ランダムな数値を生成（1-20の範囲）
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    # 減算の場合、負の数にならないように調整
    if operation['symbol'] == '-' and num1 < num2:
        num1, num2 = num2, num1

    # 正解を計算
    answer = operation['func'](num1, num2)

    # 問題文を作成
    question = f"{num1} {operation['symbol']} {num2}"

    return question, answer


def play_game():
    """クイズゲームのメイン関数"""
    print("=" * 50)
    print("🎮 2問連続正解でクリア！クイズゲーム 🎮")
    print("=" * 50)
    print()
    print("ルール:")
    print("・算数の問題が出題されます")
    print("・2問連続で正解するとクリアです")
    print("・不正解の場合は、連続正解カウントがリセットされます")
    print("・'q'を入力すると終了します")
    print()

    consecutive_correct = 0  # 連続正解数
    total_questions = 0      # 総問題数
    total_correct = 0        # 総正解数

    while consecutive_correct < 2:
        # 問題を生成
        question, correct_answer = generate_quiz()
        total_questions += 1

        # 問題を表示
        print(f"【問題 {total_questions}】")
        print(f"次の計算の答えを入力してください: {question}")
        print(f"(連続正解: {consecutive_correct}/2)")
        print()

        # ユーザーの回答を取得
        user_input = input("答え: ").strip()

        # 終了チェック
        if user_input.lower() == 'q':
            print()
            print("ゲームを終了します。")
            print(f"最終スコア: {total_correct}/{total_questions} 問正解")
            return

        # 回答をチェック
        try:
            user_answer = float(user_input)

            if user_answer == correct_answer:
                consecutive_correct += 1
                total_correct += 1
                print()
                print("✓ 正解です！")
                print()

                if consecutive_correct < 2:
                    print(f"あと {2 - consecutive_correct} 問正解でクリアです！")
                    print("-" * 50)
                    print()
            else:
                print()
                print(f"✗ 不正解です。正解は {correct_answer} でした。")
                print()

                if consecutive_correct > 0:
                    print(f"連続正解がリセットされました。")
                    consecutive_correct = 0

                print("-" * 50)
                print()

        except ValueError:
            print()
            print("✗ 無効な入力です。数値を入力してください。")
            print()
            print("-" * 50)
            print()

    # ゲームクリア
    print()
    print("🎉" * 25)
    print("🎉 おめでとうございます！2問連続正解でクリアです！ 🎉")
    print("🎉" * 25)
    print()
    print(f"最終スコア: {total_correct}/{total_questions} 問正解")
    print()


def main():
    """メインエントリーポイント"""
    while True:
        play_game()

        print()
        retry = input("もう一度プレイしますか？ (y/n): ").strip().lower()

        if retry != 'y' and retry != 'yes':
            print()
            print("ゲームを終了します。ありがとうございました！")
            break

        print()
        print()


if __name__ == "__main__":
    main()
