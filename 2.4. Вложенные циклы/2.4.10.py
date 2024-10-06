def main():
    n = int(input())
    print('А Б В')
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for p in range(1, n + 1):
                if (i + j + p == n) and i >= 1 and j >= 1 and p >= 1:
                    print(i, j, p)


if __name__ == "__main__":
    main()
