def find_minimum(lst):
    min=lst[0]
    for value in lst:
        if value<min:
            min=value
    return min

print(find_minimum([0,-1,2,3,-5,-6,-9]))
            