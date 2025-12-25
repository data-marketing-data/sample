#!/usr/bin/env python3
"""
クイズゲームのテスト
"""

import unittest
from unittest.mock import patch
from quiz_game import generate_quiz


class TestQuizGame(unittest.TestCase):
    """クイズゲームの機能をテストするクラス"""

    def test_generate_quiz_returns_tuple(self):
        """generate_quiz関数がタプルを返すことを確認"""
        result = generate_quiz()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_generate_quiz_question_format(self):
        """生成される問題が正しい形式であることを確認"""
        question, answer = generate_quiz()
        self.assertIsInstance(question, str)
        self.assertIsInstance(answer, (int, float))

    def test_generate_quiz_valid_operations(self):
        """生成される問題に有効な演算子が含まれることを確認"""
        question, answer = generate_quiz()
        valid_operators = ['+', '-', '*']
        has_valid_operator = any(op in question for op in valid_operators)
        self.assertTrue(has_valid_operator)

    def test_generate_quiz_answer_correctness(self):
        """生成された問題の答えが正しいことを確認"""
        # 複数回テストして、ランダム性があっても正しいことを確認
        for _ in range(10):
            question, expected_answer = generate_quiz()

            # 問題文をパースして検証
            parts = question.split()
            if len(parts) == 3:
                num1 = float(parts[0])
                operator = parts[1]
                num2 = float(parts[2])

                if operator == '+':
                    calculated_answer = num1 + num2
                elif operator == '-':
                    calculated_answer = num1 - num2
                elif operator == '*':
                    calculated_answer = num1 * num2
                else:
                    self.fail(f"Unknown operator: {operator}")

                self.assertEqual(expected_answer, calculated_answer,
                               f"Answer mismatch for question: {question}")

    def test_generate_quiz_no_negative_results(self):
        """減算問題で負の結果にならないことを確認"""
        # 複数回テストして確認
        for _ in range(20):
            question, answer = generate_quiz()
            if '-' in question:
                self.assertGreaterEqual(answer, 0,
                                      f"Negative result in subtraction: {question} = {answer}")


if __name__ == "__main__":
    unittest.main()
