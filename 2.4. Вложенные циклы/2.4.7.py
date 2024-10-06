def main():
    n = int(input())
    i = 3
    for t in range(1, n + 1):
        for k in range(i, 0, -1):
            print(f'До старта {k} секунд(ы)')
        print(f'Старт {t}!!!')
        i += 1


if __name__ == '__main__':
    main()
