def remove_even(lst):
    for index,value in enumerate(lst):
        if index==0:
            lst.pop(index)
        if  index<len(lst)-1:
            lst.pop(index)
            index+=2
    print('index,value',index,lst[index])
    return value

remove_even([1,5,41])