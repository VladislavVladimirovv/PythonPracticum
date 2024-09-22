def main():
    a, b, c = int(input()), int(input()), int(input())
    data = sorted([a, b, c])
    gipkv = data[0]**2 + data[1]**2
    if gipkv**0.5 == data[2]:
        print('100%')
    elif gipkv**0.5 > data[2]:
        print('крайне мала')
    else:
        print('велика')

if __name__ == "__main__":
    main()