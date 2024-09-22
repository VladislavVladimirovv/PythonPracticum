def main():
    N = int(input())
    M = int(input())
    Petya = 7 - 3 + 2 + N
    Vasya = 6 + 5 - 2 + M
    if Petya > Vasya:
        print('Петя')
    else:
        print('Вася')

if __name__ == "__main__":
    main()