class ListNode:  
    def __init__(self,val):
        self.val=val
        self.next=None

class Queue:
    def __init__(self):
        self.left=None
        self.right=None
    
    def enqueue(self,val):
        newNode=ListNode(val)
        if self.right:
            self.right.next=newNode
            self.right=self.right.next

        else:
            self.right=newNode
            self.left=self.right
    
    def print(self):
        curr=self.left
        while curr:
            print(curr.val,'->',end=' ')
            curr=curr.next

q=Queue()        
q.enqueue(5)
q.print()
            
 
        


    