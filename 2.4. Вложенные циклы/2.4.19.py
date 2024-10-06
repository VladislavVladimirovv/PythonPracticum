def main():
    n = int(input())
    k = len(str(n - n // 2))
    data = [[0 for _ in range(n)] for _ in range(n)]
    for p in range(n):
        for i in range(p, len(data) - p):
            for j in range(p, len(data) - p):
                data[i][j] += 1
    for i in range(len(data)):
        for j in range(len(data)):
            print(f'{data[i][j]:{' '}>{k}}', end=' ')
        print('')


if __name__ == '__main__':
    main()
