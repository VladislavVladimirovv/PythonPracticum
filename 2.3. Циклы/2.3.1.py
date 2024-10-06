def main():
    say = input()
    while say != 'Три!':
        print('Режим ожидания...')
        say = input()
        if say == "Три!":
            print('Ёлочка, гори!')
            break
        else:
            continue


if __name__ == '__main__':
    main()
