from typing import List

class Solution:
#Solve using 2 pointers
    def removeDuplicates(self,nums:List[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
               nums[l]=nums[r]
               l+=1
        return l
                

solution=Solution()
print(solution.removeDuplicates([1,2,3,3,4]))


        