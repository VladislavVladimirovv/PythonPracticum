def main():
    n = int(input())
    data = []
    for _ in range(n):
        data.append(int(input()))
    data.sort()
    i = 0
    delim = data[i + 1]
    nod = data[i]
    while i < n:
        while delim % nod != 0:
            delim, nod = nod, delim % nod
        i += 1
        if i < n:
            delim = data[i]
    print(nod)


if __name__ == '__main__':
    main()
