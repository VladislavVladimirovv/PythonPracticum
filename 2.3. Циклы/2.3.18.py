def main():
    def is_prime(x):
        for i in range(2, x):
            if x % i == 0:
                return 0
        return 1

    num = int(input())
    primes = []
    for i in range(2, num + 1):
        if is_prime(i):
            primes.append(i)

    i = 0
    prime = primes[i]
    divids = []
    while i < len(primes):
        if num % prime == 0:
            num //= prime
            divids.append(prime)
        elif i < len(primes) - 1:
            i += 1
            prime = primes[i]
        else:
            break
    for i in range(len(divids) - 1):
        print(divids[i], '*', end=' ')
    print(divids[-1])


if __name__ == '__main__':
    main()
