class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        array_size=len(nums1) #get the array length to use in while loop
        i=m-1 #pointer to start at '0' position
        j=n
        while i<array_size:
            if nums1[i-1]<=nums2[j]:
                nums1[i]=nums2[j]:
            else:
                temp=nums1[i-1]
                nums1[i-1]=nums1[j]
                nums1[i]=temp
                

            




        

    


        
    
    
        