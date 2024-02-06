def generator_squares(N):
    for i in range(N):
        yield i ** 2

N = int(input())
generated_squares = generator_squares(N)

for square in generated_squares:
    print(square)