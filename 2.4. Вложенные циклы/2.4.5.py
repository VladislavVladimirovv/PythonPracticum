def main():
    n = int(input())
    counter = 0
    for _ in range(n):
        flag = False
        data = input()
        while data != 'ВСЁ':
            if data == 'зайка':
                flag = True
            data = input()
        if flag:
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
