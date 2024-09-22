def main():
    a, b, c = int(input()), int(input()), int(input())
    if a % 10 == b % 10 == c % 10:
        print(a % 10)
    else:
        print(a // 10)

if __name__ == "__main__":
    main()