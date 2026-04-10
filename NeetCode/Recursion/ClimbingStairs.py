class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=0:
            return None
        previous,current=1,1
        for i in range(n-1):
            temp=current
            current=current+previous
            previous=temp
        return current
    

s1=Solution()
print('total ways',s1.climbStairs(4))