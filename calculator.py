#!/usr/bin/env python3
"""
算数計算機 (Arithmetic Calculator)

このプログラムは基本的な算数演算を提供します。
加算、減算、乗算、除算をサポートしています。
"""


def add(a, b):
    """2つの数を加算する"""
    return a + b


def subtract(a, b):
    """2つの数を減算する (a - b)"""
    return a - b


def multiply(a, b):
    """2つの数を乗算する"""
    return a * b


def divide(a, b):
    """2つの数を除算する (a / b)"""
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b


def main():
    """メインプログラム - 対話的な計算機"""
    print("=== 算数計算機 ===")
    print("利用可能な演算:")
    print("1. 加算 (+)")
    print("2. 減算 (-)")
    print("3. 乗算 (*)")
    print("4. 除算 (/)")
    print("5. 終了 (q)")
    print()

    while True:
        operation = input("演算を選択してください (1-5): ").strip()

        if operation == '5' or operation.lower() == 'q':
            print("計算機を終了します。")
            break

        if operation not in ['1', '2', '3', '4']:
            print("無効な選択です。1-5の間で選択してください。")
            continue

        try:
            num1 = float(input("最初の数を入力してください: "))
            num2 = float(input("2番目の数を入力してください: "))

            if operation == '1':
                result = add(num1, num2)
                print(f"結果: {num1} + {num2} = {result}")
            elif operation == '2':
                result = subtract(num1, num2)
                print(f"結果: {num1} - {num2} = {result}")
            elif operation == '3':
                result = multiply(num1, num2)
                print(f"結果: {num1} * {num2} = {result}")
            elif operation == '4':
                result = divide(num1, num2)
                print(f"結果: {num1} / {num2} = {result}")

            print()

        except ValueError as e:
            print(f"エラー: {e}")
            print()
        except Exception as e:
            print(f"予期しないエラーが発生しました: {e}")
            print()


if __name__ == "__main__":
    main()
