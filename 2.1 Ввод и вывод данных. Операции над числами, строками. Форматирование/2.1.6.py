def main():
    things = input()
    sale = int(input())
    waight = int(input())
    money = int(input())
    print('Чек')
    print(things, ' - ', waight, 'кг', ' - ', sale, 'руб/кг', sep='')
    print('Итого: ', waight * sale, 'руб', sep='')
    print('Внесено: ', money, 'руб', sep='')
    print('Сдача: ', money - waight * sale, 'руб', sep='')

if __name__ == "__main__":
    main()