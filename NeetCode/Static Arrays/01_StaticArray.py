#Initialize Array
arr=[1,3,5,7,8]
#Traversing through an array
#Range function in python range(start,end,step)
#by default start=0 and step=1 ; 
# End is required --
#An integer number specifying at which position to stop (not included).
########For Loop Traversal##########
for i in range(len(arr)):
    print(arr[i])
########While Loop Traversal##########
i=0
while i<len(arr):
    print(arr[i])
    i+=1
#######################################

#Deleting from end of an array
'''
length=len(arr)
arr[length-1]=None
print(arr)'''

#Deleting at ith index
def deleteatindex(arr,index):
    length=len(arr)
    for i in range(index+1,len(arr)):
        arr[i-1]=arr[i]
    arr[length-1]=None
    return arr
