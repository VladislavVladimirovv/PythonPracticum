def main():
    def NOD(x, y):
        for i in range(min(x, y), 0, -1):
            if x % i == 0 and y % i == 0:
                return i
        return 1

    x = int(input())
    y = int(input())
    print(NOD(x, y))


if __name__ == '__main__':
    main()
