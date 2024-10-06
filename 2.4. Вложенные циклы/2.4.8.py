def main():
    def sum_dig(num):
        total = 0
        for dig in num:
            total += int(dig)
        return total

    n = int(input())
    winer = ''
    max_sum_dig = 0
    for _ in range(n):
        name = input()
        x = input()
        a = sum_dig(x)
        if a >= max_sum_dig:
            max_sum_dig = a
            winer = name
    print(winer)


if __name__ == '__main__':
    main()
