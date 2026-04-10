def mergesort(arr,s,e):
    if e-s+1<=1:
        return arr
    m=(s+e)//2
    mergesort(arr,s,m)
    mergesort(arr,m+1,e)
    merge(arr,s,m,e)
    return arr

def merge(arr,s,m,e):
    L=arr[s:m+1]
    R=arr[m+1:e+1]
    i=0
    j=0
    k=s
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:   #Left array less than right array
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    
    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1
   
        

print(mergesort([3,2,4,1,6],0,4))
