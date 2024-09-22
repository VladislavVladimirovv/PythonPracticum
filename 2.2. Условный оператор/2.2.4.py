def main():
    v1, v2, v3 = [int(input()), 'Петя'], [int(input()), 'Вася'], [int(input()), 'Толя']
    winers = sorted([v1, v2, v3], reverse=True)
    for i in range(3):
        print(f'{i + 1}. {winers[i][1]}')

if __name__ == "__main__":
    main()