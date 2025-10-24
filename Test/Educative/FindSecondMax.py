def find_second_maximum(nums):
    first_max=second_max=float('-inf')
    for i in range(len(nums)):
        if nums[i]>first_max:
            second_max=first_max
            first_max=nums[i]
        if nums[i]<first_max:
            if nums[i]>second_max:
                second_max=nums[i]
    return second_max
    print('first_max',first_max,'second_max',second_max)
print('second max',find_second_maximum([1,6,-8,-10,3]))