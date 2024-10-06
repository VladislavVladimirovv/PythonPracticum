def main():
    data = input()
    num = ''
    for i in range(len(data)):
        if int(data[i]) % 2 != 0:
            num += data[i]
    print(num)


if __name__ == '__main__':
    main()
