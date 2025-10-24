def rearrange_list(nums):
    length=len(nums)-1
    i=0
    mid_point=length//2
    new_list=[]
    while length>= mid_point:
        new_list.append(nums[length])
        if i< mid_point:
            new_list.append(nums[i])
        length-=1
        i=i+1
    return new_list

def main():
    print(rearrange_list([1,2,3,4,5,6,7,8,9,10]))

if __name__ == "__main__":
    main()
