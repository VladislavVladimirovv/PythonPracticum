def main():
    a = int(input())
    b = int(input())
    data = input()
    if len(data) % 6 == 0:
        print(a + b)
    elif len(data) % 3 == 0:
        print(a - b)
    elif len(data) % 2 == 0:
        print(a * b)
    else:
        print(a // b)


if __name__ == "__main__":
    main()
