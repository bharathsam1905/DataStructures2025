from Node import Node
class LinkedList:
    def __init__(self):
        self.head_node=None #Pointer to the first Node 

    def get_head_node(self):
        return self.head_node
    
    def is_empty(self):
        return self.head_node is None
    
    def insert_at_head(self,data):
        temp_node=Node(data)
        temp_node.next_element=self.head_node
        self.head_node=temp_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
            return
        tail = self.head_node
        while tail.next_element is not None:
            tail = tail.next_element
        tail.next_element = new_node
     
    def search(self, value):
        current_node=self.head_node
        while current_node is not None:
            if current_node.data==value:
             return True
            current_node=current_node.next_element
        return False
    
    def delete(self,value):
        current_node=self.head_node
        if current_node is None:
            return
        if current_node.data==value:
            self.head_node=current_node.next_element
            return
        while current_node is not None and current_node.next_element is not None:
            if current_node.next_element.data==value:
                current_node.next_element=current_node.next_element.next_element
                return
            current_node=current_node.next_element
        
    def length_of_linkedlist(self):
        length=0
        current_node=self.head_node
        if current_node is None:
            return 0
        while current_node is not None:
            length+=1
            current_node=current_node.next_element
        return length
      
    def print_linkedlist(self):
        current = self.head_node
        if current is None:
            print("List is empty")
            return
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next_element
        print("None")  # Marks end of list







    

