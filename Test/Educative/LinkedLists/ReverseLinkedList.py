from SinglyLinkedList import LinkedList

def reverse_linked_list(self,linkedlist1):
    while linkedlist1 is not None:
        if linkedlist1.next_element==None:
            self.head=linkedlist1
    reverse_node=self.head
    while linkedlist1 is not None:
        if reverse_node.data==linkedlist1.next_element.data:
            reverse_node.next_element=linkedlist1
            reverse_node.next_element=reverse_node.next_element.next_element

        linkedlist1=linkedlist1.next_element
    
    return reverse_node


