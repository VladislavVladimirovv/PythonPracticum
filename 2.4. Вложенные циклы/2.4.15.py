def main():
    n = int(input())
    m = int(input())
    k1 = n * 2 - 1
    k2 = 1
    t = len(str(n * m))
    for i in range(1, n + 1):
        s = 1
        num = i
        for j in range(m):
            print(f'{num:{' '}>{t}}', end=' ')
            if s == 1:
                num += k1
                s = 2
            else:
                num += k2
                s = 1
        print('')
        k1 -= 2
        k2 += 2


if __name__ == '__main__':
    main()
