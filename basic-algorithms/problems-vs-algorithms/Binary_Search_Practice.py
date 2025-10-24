def binary_search(array,target):
    low=0
    high=len(array)-1
    while low<=high:
        mid_index=(low+high)//2
        print('mid_index',mid_index)
        if array[mid_index]==target:
            return mid_index
        elif array[mid_index]<target:
            low=mid_index+1
        else:
            high=mid_index-1
    return -1
    

        
 

print('location',binary_search([1,5,9,15,17],17))

    
    