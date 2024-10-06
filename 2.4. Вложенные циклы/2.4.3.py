def main():
    n = int(input())
    m = 1
    k = 1
    while m <= n:
        for i in range(k):
            if m <= n:
                print(m, end=' ')
                m += 1
            else:
                break
        print('')
        k += 1

if __name__ == '__main__':
    main()