def main():
    n = int(input())
    m = int(input())
    p = len(str(n * m))
    for i in range(1, n + 1):
        num = i
        for k in range(1, m + 1):
            print(f'{num:>{''}{p}}', end=' ')
            num += n
        print('')


if __name__ == '__main__':
    main()
