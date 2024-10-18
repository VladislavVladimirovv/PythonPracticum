def main():
    n = int(input())
    data = []
    for _ in range(n):
        data.append(int(input()))
    min_ch = 10 ** 9
    for i in range(1, n):
        if data[i] > data[i - 1]:
            min_ch = min(min_ch, data[i])
    print(min_ch)


if __name__ == "__main__":
    main()
