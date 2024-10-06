def main():
    n = int(input())
    p = int(input())
    for i in range(1, n + 1):
        for m in range(1, n + 1):
            print(f'{i * m:^{' '}{p - 1}}', end=' ')
            if m != n:
                print('|', end='')
        print('')
        if i != n:
            print('-' * p * n, '-' * (n - 1), sep='')


if __name__ == '__main__':
    main()
