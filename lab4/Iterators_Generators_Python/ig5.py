def countdown(N):
    while N >= 0:
        yield N
        N -= 1

N = int(input())

countd = countdown(N)

countdo = ', '.join(map(str,countd))

print(countdo)