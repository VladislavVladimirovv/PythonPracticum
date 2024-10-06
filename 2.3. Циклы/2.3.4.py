def main():
    a = int(input())
    b = int(input())
    if a < b:
        while a <= b:
            print(a, end=' ')
            a += 1
    else:
        while a >= b:
            print(a, end=' ')
            a -= 1


if __name__ == "__main__":
    main()
