def main():
    print('Как Вас зовут?')
    name = input()
    print(f'Здравствуйте, {name}!')
    print('Как дела?')
    answer = input()
    if answer == 'хорошо':
        print('Я за вас рада!')
    else:
        print('Всё наладится!')

if __name__ == "__main__":
    main()