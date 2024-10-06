def main():
    def is_prime(x):
        if x == 0 or x == 1:
            return 0
        for i in range(2, x):
            if x % i == 0:
                return 0
        return 1

    n = int(input())
    counter = 0
    for k in range(n):
        num = int(input())
        if is_prime(num):
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
