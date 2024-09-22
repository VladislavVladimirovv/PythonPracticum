def main():
    data = int(input())
    a, b, c = data // 100, (data % 100) // 10, data % 10
    A = sorted([a, b, c])
    if A[0] + A[2] == A[1] * 2:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()

