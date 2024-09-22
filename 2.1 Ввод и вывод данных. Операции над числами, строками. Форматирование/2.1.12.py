num1, num2 = int(input()), int(input())
a, b, c = num1 // 100, (num1 % 100) // 10, num1 % 10
a2, b2, c2 = num2 // 100, (num2 % 100) // 10, num2 % 10
print((a + a2) % 10, (b + b2) % 10, (c + c2) % 10, sep='')