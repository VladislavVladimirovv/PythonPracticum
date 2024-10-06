def main():
    data = input()
    if data[::-1] == data:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
