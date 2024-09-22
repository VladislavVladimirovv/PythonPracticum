def main():
    string = input()
    if string == string[::-1]:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()