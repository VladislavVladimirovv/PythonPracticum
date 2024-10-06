def main():
    def is_prime(x):
        if x == 1 or x == 0:
            return "NO"
        for i in range(2, x):
            if x % i == 0:
                return 'NO'
        return "YES"

    print(is_prime(int(input())))


if __name__ == '__main__':
    main()
