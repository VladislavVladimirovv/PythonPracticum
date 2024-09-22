def main():
    data = int(input())
    u1 = data % 10 + (data % 100) // 10
    u2 = data // 100 + (data % 100) // 10
    print(max(u1, u2), min(u1, u2), sep='')

if __name__ == "__main__":
    main()