def main():
    n = int(input())
    names = [input() for _ in range(n)]
    print(sorted(names)[0])


if __name__ == '__main__':
    main()
