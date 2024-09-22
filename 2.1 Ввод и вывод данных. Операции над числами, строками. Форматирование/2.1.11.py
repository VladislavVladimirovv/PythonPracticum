num = int(input())
a, b, c, d = num // 1000, (num % 1000) // 100, (num % 100) // 10, num % 10
print(b, a, d, c, sep='')