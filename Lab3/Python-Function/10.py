def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

lst = [1,2,2,3,4,5,6,6]
print(unique_list(lst))