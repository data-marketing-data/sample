# 算数計算機 (Arithmetic Calculator)

基本的な算数演算を行うPythonプログラムです。

## 機能

- **加算** (+): 2つの数を足します
- **減算** (-): 2つの数を引きます
- **乗算** (*): 2つの数を掛けます
- **除算** (/): 2つの数で割ります（0除算チェック付き）

## 使い方

### 対話的モードで実行

```bash
python3 calculator.py
```

プログラムを実行すると、メニューが表示され、演算を選択して計算できます。

### Pythonモジュールとして使用

```python
from calculator import add, subtract, multiply, divide

# 加算
result = add(5, 3)  # 8

# 減算
result = subtract(10, 4)  # 6

# 乗算
result = multiply(3, 7)  # 21

# 除算
result = divide(20, 4)  # 5.0
```

## テストの実行

```bash
python3 test_calculator.py
```

または、詳細な出力付きで実行:

```bash
python3 test_calculator.py -v
```

## 例

```
=== 算数計算機 ===
利用可能な演算:
1. 加算 (+)
2. 減算 (-)
3. 乗算 (*)
4. 除算 (/)
5. 終了 (q)

演算を選択してください (1-5): 1
最初の数を入力してください: 15
2番目の数を入力してください: 7
結果: 15.0 + 7.0 = 22.0
```

## 要件

- Python 3.x

## ライセンス

このプロジェクトはオープンソースです。
