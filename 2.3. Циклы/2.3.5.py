def main():
    thing = float(input())
    summa = 0
    while thing != 0:
        if thing < 500:
            summa += thing
        else:
            summa += thing * 0.9
        thing = float(input())
    print(summa)


if __name__ == '__main__':
    main()
