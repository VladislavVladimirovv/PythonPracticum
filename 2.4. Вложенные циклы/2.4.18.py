def main():
    n = int(input())
    m = 1
    i = 1
    data = []
    max_data = ''
    while m <= n:
        data = ''
        for k in range(i):
            if m <= n:
                data += str(m) + ' '
                m += 1
            else:
                break
        i += 1
        if len(max_data) < len(data):
            max_data = data

    m = 1
    i = 1
    data = []
    while m <= n:
        data = ''
        for k in range(i):
            if m <= n:
                data += str(m) + ' '
                m += 1
            else:
                break
        print(f'{data:^{''}{len(max_data)}}')
        i += 1


if __name__ == '__main__':
    main()
