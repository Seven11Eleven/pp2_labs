def squares(a, b):
    while a <= b:
        yield a ** 2
        a += 1

a = int(input())
b = int(input())

squaress = squares(a, b)

for i in squaress:
    print(i)