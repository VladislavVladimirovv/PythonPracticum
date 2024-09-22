def main():
    a = input()
    b = input()
    data = [int(x) for x in a + b]
    data.sort()
    print(data[-1], sum(data[1:-1]) % 10, data[0], sep='')

if __name__ == "__main__":
    main()