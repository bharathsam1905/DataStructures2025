from typing import List
def InsertionSort(arr:List[int])->list:
    for i in range(1,len(arr)):
        j=i-1
        while j>=0 and arr[j+1]<arr[j]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
            j=j-1
    return arr


print(InsertionSort([1,9,4,8]))