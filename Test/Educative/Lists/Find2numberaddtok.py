def find2numbersaddtok(num,k):
    result=[]
    num.sort()
    left=0
    right=len(num)-1
    for i in range(len(num)):
        sum=num[left]+num[right]
        if sum<k:
            left+=1
        elif sum>k:
            right-=1
        else:
            result.append(num[left])
            result.append(num[right])                    
            return result
        
        


def main():
    print(find2numbersaddtok([1,7,4,6,5,9],11))

if __name__=="__main__":
    main()
    
    