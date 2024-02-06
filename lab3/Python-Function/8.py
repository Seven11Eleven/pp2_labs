def spy_game(nums):
    for i in range(len(nums)):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False
print(spy_game([1, 2, 0, 0, 8, 8, 9]))