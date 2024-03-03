import time

root = float(input())
ms = float(input())

time.sleep(ms / 1000)
print(f"Square rot of {int(root)} after {int(ms)} miliseconds is {root**(1/2)}")