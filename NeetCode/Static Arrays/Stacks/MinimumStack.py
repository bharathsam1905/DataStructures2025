class MinStack:
    def __init__(self):
        self.stack=[] #Initialize Stack
        self.minstack=[] #keeps the min value

    
    def push(self,val:int)-> None:
        self.stack.append(val)
        val=min(val,self.minstack[-1] if self.minstack else val)       
        self.minstack.append(val)
    def pop(self) -> None:
            self.minstack.pop()
            self.stack.pop()

    
    def top(self)->int:
        return self.stack[-1]
    
    def getMin(self)->int:
        if self.minstack:
            return self.minstack[-1]
        else:
            return 0


minStack = MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
print('get min first time',minStack.getMin()); # return 0
minStack.pop();
minStack.top();    # return 2
print('get min second time',minStack.getMin()); # return 1
