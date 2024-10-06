def main():
    n = int(input())
    hn = [0] * (n + 1)
    bns = []
    for i in range(1, n + 1):
        bn = int(input())
        imhn = bn % 256
        mn = bn // 256 ** 2
        rn = (bn // 256) % 256
        rehn = (37 * (mn + rn + hn[i - 1])) % 256
        hn[i] = rehn
        if imhn == rehn and rehn < 100:
            bns.append('YES')
        else:
            bns.append('NO')
    if "NO" in bns:
        print(bns.index("NO"))
    else:
        print(-1)


if __name__ == '__main__':
    main()
