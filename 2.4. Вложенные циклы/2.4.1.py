def main():
    n = int(input())
    for i in range(1, n + 1):
        for m in range(1, n + 1):
            print(i * m, end=' ')
        print('')


if __name__ == "__main__":
    main()
