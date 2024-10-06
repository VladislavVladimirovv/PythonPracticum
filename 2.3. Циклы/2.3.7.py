def main():
    def NOK(a, b):
        x = min(a, b)
        y = max(a, b)
        for i in range(1, x + 1):
            if (y * i) % x == 0:
                return i * y
        return 0

    first = int(input())
    second = int(input())
    print(NOK(first, second))


if __name__ == '__main__':
    main()
