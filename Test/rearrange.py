def rearrange(lst):
    new_list = []
    for item in lst:
        if item<0:
            new_list.append(item)
    for item in lst:
        if item>=0:
            new_list.append(item)
    return new_list

print (rearrange([3, -2, 5, 1, 0, -1, 4]))  # Output: [-2, -5, -1, 3, 1, 0, 4]
