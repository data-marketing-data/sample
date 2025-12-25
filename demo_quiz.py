#!/usr/bin/env python3
"""
クイズゲームのデモ実行スクリプト
自動で問題を解いてクリアする様子を表示します
"""

import time
from quiz_game import generate_quiz

def demo_play():
    """デモプレイを実行"""
    print("=" * 50)
    print("🎮 2問連続正解でクリア！クイズゲーム 🎮")
    print("=" * 50)
    print()
    print("ルール:")
    print("・算数の問題が出題されます")
    print("・2問連続で正解するとクリアです")
    print("・不正解の場合は、連続正解カウントがリセットされます")
    print()
    print("【デモモード】自動で問題を解きます...")
    print()
    time.sleep(2)

    consecutive_correct = 0
    total_questions = 0
    total_correct = 0

    while consecutive_correct < 2:
        question, correct_answer = generate_quiz()
        total_questions += 1

        print(f"【問題 {total_questions}】")
        print(f"次の計算の答えを入力してください: {question}")
        print(f"(連続正解: {consecutive_correct}/2)")
        print()

        # 自動で正解を入力
        time.sleep(1)
        print(f"答え: {correct_answer}")
        time.sleep(0.5)

        consecutive_correct += 1
        total_correct += 1
        print()
        print("✓ 正解です！")
        print()

        if consecutive_correct < 2:
            print(f"あと {2 - consecutive_correct} 問正解でクリアです！")
            print("-" * 50)
            print()
            time.sleep(1)

    # ゲームクリア
    print()
    print("🎉" * 25)
    print("🎉 おめでとうございます！2問連続正解でクリアです！ 🎉")
    print("🎉" * 25)
    print()
    print(f"最終スコア: {total_correct}/{total_questions} 問正解")
    print()

if __name__ == "__main__":
    demo_play()
