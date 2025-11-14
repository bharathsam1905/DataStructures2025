def find_max_sum_sublist(nums):
    curr_sum=0
    store_max=nums[0]
    for i in nums:
        if i<=curr_sum+i:
            curr_sum+=i
        elif i>curr_sum+i:
            curr_sum=i
        if store_max<curr_sum:
              store_max=curr_sum      

 
    return store_max
        

print(find_max_sum_sublist([-2,1,-3,4,-1,2,1,-5,4]))

