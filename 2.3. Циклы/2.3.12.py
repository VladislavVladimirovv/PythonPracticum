def main():
    num = input()
    max_c = 0
    for i in num:
        max_c = max(max_c, int(i))
    print(max_c)


if __name__ == '__main__':
    main()
