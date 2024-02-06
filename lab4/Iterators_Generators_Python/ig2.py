def generator_even(N):
    for i in range(0, N + 1, 2):
        yield i

N = int(input())
generated_even = generator_even(N)

square = ', '.join(map(str, generated_even))
print(square)