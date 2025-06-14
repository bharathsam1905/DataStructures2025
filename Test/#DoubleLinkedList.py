#DoubleLinkedList
class DoubleNode:
    def __init__(self,value):
        self.value=value
        self.head=None
        self.tail=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def append(self,value):
        if self.head==None:
            self.head=DoubleNode(value)
            self.tail=self.head
        
        self.tail.next=DoubleNode(value)
        self.tail.next.previous=self.tail
        self.tail=self.tail.next
        return
    
linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous
            
            