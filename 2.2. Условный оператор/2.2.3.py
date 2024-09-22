def main():
    v1, v2, v3 = [int(input()), 'Петя'], [int(input()), 'Вася'], [int(input()), 'Толя']
    print(max([v1, v2, v3])[1])

if __name__ == "__main__":
    main()