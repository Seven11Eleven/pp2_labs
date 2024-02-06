def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

spisok = [3,2,4,1,5,2,3,5,11,3,3,4,22,3,13,14,15,1337,132,12]

prosto_spisok = list(filter(lambda x: is_prime(x), spisok))
print(sorted(prosto_spisok))