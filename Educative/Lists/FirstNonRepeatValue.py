def find_first_unique(nums):
    nums.sort()
    length = len(nums)
    left = 0
    right = 0

    for i in range(length - 1):
        left = i - 1
        right = i + 1

        # first element
        if left < 0 and nums[i] != nums[right]:
            return nums[i]

        # middle elements
        if left >= 0 and nums[i] != nums[left] and nums[i] != nums[right]:
            return nums[i]

    # check the last element outside loop
    if nums[length - 1] != nums[length - 2]:
        return nums[length - 1]
    if length==1:
        return nums[0]

    return None


print(find_first_unique([2, 2, 2, 3, 5, 3,8,8,5,9]))
