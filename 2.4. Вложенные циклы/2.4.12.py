def main():
    n = int(input())
    m = int(input())
    p = len(str(m * n))
    num = 0
    for i in range(n):
        for j in range(m):
            num += 1
            print(f'{num:{' '}>{p}}', end=' ')
        print('')


if __name__ == '__main__':
    main()
