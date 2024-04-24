#1211201118 林優花
import cmath

def solve_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "不定"  # 解が不定の場合
            else:
                return "解なし"  # 解が存在しない場合
        else:
            return [-c / b]  # 一次方程式の解をリストで返す

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return [x1, x2]  # 解をリストで返す
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]  # 解をリストで返す
    else:
        x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return [x1, x2]  # 解をリストで返す

# 確認用スクリプト
if __name__ == '__main__':
    # 二次方程式の係数
    a = 1
    b = 2
    c = 1

    # 二次方程式の解の計算
    solutions = solve_quadratic_equation(a, b, c)

    # 解の出力
    print("解:")
    if isinstance(solutions, str):
        print(solutions)
    else:
        for solution in solutions:
            print(solution)
