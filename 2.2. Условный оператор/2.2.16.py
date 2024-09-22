def main():
    data = [[int(input()), 'Петя'], [int(input()), 'Вася'], [int(input()), 'Толя']]
    data.sort(reverse=True)
    print(data[0][1].center(24))
    print(data[1][1].center(8))
    print(' ' * 16, data[2][1].center(8), sep='')
    print('II'.center(8), end='')
    print('I'.center(8), end='')
    print('III'.center(8), end='')

if __name__ == "__main__":
    main()