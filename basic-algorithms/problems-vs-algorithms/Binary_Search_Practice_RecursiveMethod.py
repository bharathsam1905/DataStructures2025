def bsr (array,search_element,start=0,end=None):
    if end is None:    
        end=len(array)-1
    if start>end:
        return -1
    mid =(start+end)//2
    if array[mid]==search_element: 
        return mid
       
    elif array[mid]<search_element:
       start=mid+1          
    else:
        end=mid-1
    return bsr(array,search_element,start,end)


print('find element',bsr([21,22,23,24,25],25))