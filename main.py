from math import sqrt


def solve_quadratic_equation(a: float, b: float, c: float) -> list:
    try:
        if b == 0 and a == 0:
            return ["не уравнение"]

        if a == 0:
            return [-c / b]

        discr = b * b - 4 * a * c

        if discr > 0:
            x1 = (-b + sqrt(discr)) / (2 * a)
            x2 = (-b - sqrt(discr)) / (2 * a)
            return [x1, x2]
        elif discr < 0:
            return ["нет корней"]
        elif discr == 0:
            return [-b / (2 * a)]
    except:
        raise TypeError


def main():
    result = solve_quadratic_equation(1, -4, -5)

    for i in range(len(result)):
        if type(result[i]) == float:
            print(f"x{i+1} = {result[i]}")
        else:
            print(f"{result[i]}")


if __name__ == '__main__':
    main()
