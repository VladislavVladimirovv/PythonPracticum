def main():
    name = input()
    data = int(input())
    print('Группа №', data // 100, '.', sep='')
    print(data % 10, '. ', name, '.', sep='')
    print('Шкафчик: ', data, '.', sep='')
    print('Кроватка: ', (data % 100) // 10, '.', sep='')

if __name__ == "__main__":
    main()