from math import *


def main():
    num = 500
    a = ceil(num / 2)
    print(num)
    say = input()
    while say != 'Угадал!':
        if say == 'Больше':
            num = num + a
            if a > 1:
                a = ceil(a / 2)
        elif say == "Меньше":
            num = num - a
            if a > 1:
                a = ceil(a / 2)
        print(num)
        say = input()


if __name__ == '__main__':
    main()
