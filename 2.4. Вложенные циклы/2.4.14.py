def main():
    n = int(input())
    m = int(input())
    p = len(str(m * n))
    num = 0
    y = 1
    for i in range(n):
        data = []
        for j in range(m):
            num += 1
            data.append(f'{num:{' '}>{p}}')
        print(*data[::y])
        y *= -1


if __name__ == '__main__':
    main()
