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
    
    def dequeue(self):
        if not self.left:
            return None
        val=self.left.val
        self.left=self.left.next
        if not self.left:
            self.right=None
        return val

    
    def print(self):
        curr=self.left
        while curr:
            print(curr.val,'->',end=' ')
            curr=curr.next
        print()

q=Queue()        
q.enqueue(5)
q.enqueue(8)
q.enqueue(9)
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()
            
 
        


    