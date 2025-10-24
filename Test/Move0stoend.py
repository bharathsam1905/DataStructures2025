def movezeroestoend(arr):
    length=len(arr)
    if length<2:
        return arr
    counter=0
    for index,value in enumerate(arr):
        if value!=0:
            arr[counter]=value
            counter+=1
    
    while counter<length:
        arr[counter]=0
        counter+=1

    return arr

print(movezeroestoend([1,5,80,0,7,0,6,0,5]))