def main():
    def max_dig(num):
        return max([int(x) for x in num])

    n = int(input())
    s = ''
    for _ in range(n):
        a = input()
        s += str(max_dig(a))
    print(s)


if __name__ == '__main__':
    main()
