def main():
    N, M, k1, k2 = int(input()), int(input()), int(input()), int(input())
    m = N * (M - k1) // (k2 - k1)
    n = N - m
    print(n, m)

if __name__ == "__main__":
    main()