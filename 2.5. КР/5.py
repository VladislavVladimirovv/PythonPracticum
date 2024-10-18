def main():
    n = int(input())
    srzn = []
    for i in range(n):
        data = input()
        counter = 0
        summa = 0
        while data != 'stop':
            data = int(data)
            summa += data
            counter += 1
            data = input()
        srzn.append(summa / counter)
    print(round(sum(srzn), 2))


if __name__ == "__main__":
    main()
