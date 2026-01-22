from typing import List
class Solution:
    def isValid(self,s:str)->bool:
        Stack=[]
        mapping={')':'(',']':'[','}':'{'}
        length=len(s)
        if length==0:
            return True
        for i in range(length):
            if s[i] in '([{':
                Stack.append(s[i])
            else:
                if s[i]==')' and len(Stack)>0 and Stack[len(Stack)-1]=='(':
                    Stack.pop()
                elif s[i]==']' and len(Stack)>0 and Stack[len(Stack)-1]=='[':
                    Stack.pop()
                elif s[i]=='}' and len(Stack)>0 and Stack[len(Stack)-1]=='{':
                    Stack.pop()
                else:
                    return False
        if len(Stack)==0:
             return True
        else:
             return False

            
sol=Solution()
print(sol.isValid('[(])'))