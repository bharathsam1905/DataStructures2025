def right_rotate(nums, k):
    new_array=[]
    if len(nums)==0:
        return []
    k%=len(nums)
    new_array=nums[-k:]+nums[:-k]
    return new_array

print(right_rotate([1,2,4,-6,7,8],4))
        