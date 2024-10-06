def main():
    cmd = input()
    n = int(input())
    x = 0
    y = 0
    while cmd != 'СТОП':
        if cmd == "СЕВЕР":
            x += n
        elif cmd == 'ЮГ':
            x -= n
        elif cmd == "ЗАПАД":
            y -= n
        elif cmd == 'ВОСТОК':
            y += n
        cmd = input()
        if cmd == 'СТОП':
            break
        else:
            n = int(input())
    print(x)
    print(y)


if __name__ == '__main__':
    main()
