from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for i in nums:
            if i==val:
                continue
            else:
                nums[l]=i
                l+=1
        return l



# Example usage:
solution = Solution()
nums = [3, 2, 2, 3]
val = 3
new_length = solution.removeElement(nums, val)
print(f"New length: {new_length}, Modified array: {nums[:new_length]}") 
# Output: New length: 2, Modified array: [2, 2]