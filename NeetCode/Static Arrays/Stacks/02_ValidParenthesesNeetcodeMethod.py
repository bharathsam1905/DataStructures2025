class Solution:
    def isValid(self,s:str)->bool:
        dict_valid={
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack=[]
        for ch in s:
            if ch in dict_valid:
                if stack and stack[-1]==dict_valid[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack

solution=Solution()
print(solution.isValid('[()]'))

    

