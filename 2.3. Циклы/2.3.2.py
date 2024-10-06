def main():
    say = input()
    counter = 0
    while say != 'Приехали!':
        counter += say.count('зайка')
        say = input()
    print(counter)


if __name__ == '__main__':
    main()
