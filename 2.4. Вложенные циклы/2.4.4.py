def main():
    n = int(input())
    total = 0
    for _ in range(n):
        data = input()
        for x in data:
            total += int(x)
    print(total)


if __name__ == "__main__":
    main()
