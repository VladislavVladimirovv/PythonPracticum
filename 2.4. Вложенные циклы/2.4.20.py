def main():
    n = int(input())
    ss = [sum(int(x) for x in str(n)), 10]
    for i in range(2, 10):
        num = n
        tot_dig = num % i
        num = num // i
        while num != 0:
            tot_dig += num % i
            num = num // i
        if (ss[0] < tot_dig) or (ss[0] == tot_dig and ss[1] > i):
            ss = [tot_dig, i]
    print(ss[1])


if __name__ == '__main__':
    main()
