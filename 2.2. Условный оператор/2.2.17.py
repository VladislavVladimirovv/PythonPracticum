def main():
    a, b, c = float(input()), float(input()), float(input())
    D = b ** 2 - 4 * a * c
    if a == b == c == 0:
        print('Infinite solutions')
    elif a == 0 and b != 0:
        print(-c / b)
    elif D > 0 and a != 0:
        x1 = round((-b + D ** 0.5) / (2 * a), 2)
        x2 = round((-b - D ** 0.5) / (2 * a), 2)
        print(min(x1, x2), max(x1, x2))
    elif D == 0 and a != 0:
        print(round(-b / (2 * a), 2))
    else:
        print('No solution')

if __name__ == "__main__":
    main()