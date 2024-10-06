def main():
    n = int(input())
    counter = 0
    for _ in range(n):
        data = input()
        if "зайка" in data:
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
