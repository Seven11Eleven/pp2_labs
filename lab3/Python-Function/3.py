def solve(numheads, numlegs):
    num_rabbits = (numlegs - 2 * numheads)/2
    num_chickens = numheads - num_rabbits
    return num_rabbits, num_chickens
print(solve(35, 94))