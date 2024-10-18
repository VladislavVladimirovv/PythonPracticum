def main():
    n = int(input())
    m = int(input())
    for i in range(n, m - 1, -int((n - m) / 3)):
        print(i, end='')
        if (i - (n - m) // 3) > m - 1:
            print(';', end=' ')
    print('')
    print('Старт!')


if __name__ == "__main__":
    main()
