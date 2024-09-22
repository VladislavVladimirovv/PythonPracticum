def main():
    a, b, c = input(), input(), input()
    data = sorted([a, b, c])
    for i in data:
        if 'зайка' in i:
            print(i, len(i))
            break

if __name__ == "__main__":
    main()