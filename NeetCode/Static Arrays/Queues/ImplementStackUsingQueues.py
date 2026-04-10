from collections import deque

class MyStack:

    def __init__(self):
        self.q=deque()
      
    def push(self, x: int) -> None:
        self.q.append(x)
        
        

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()
            
       
       
    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q)==0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
obj.push(6)
obj.push(7)
print('top value:',obj.top())
param_2 = obj.pop()
print('popped element',param_2)
