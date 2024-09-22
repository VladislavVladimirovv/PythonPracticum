def main():
    thing, sale, waight, money = input(), int(input()), int(input()), int(input())
    print('=' * 16, 'Чек', '=' * 16, sep='')
    print('Товар:', thing.rjust(29, ' '), sep='')
    print('Цена:', f'{waight}кг * {sale}руб/кг'.rjust(30, ' '), sep='')
    print('Итого:', f'{str(waight * sale)}руб'.rjust(29, ' '), sep='')
    print('Внесено:', f'{str(money)}руб'.rjust(27, ' '), sep='')
    print('Сдача:', f'{str(money - waight * sale)}руб'.rjust(29, ' '), sep='')
    print('=' * 35, sep='')

if __name__ == "__main__":
    main()