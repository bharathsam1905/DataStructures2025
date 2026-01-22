from SinglyLinkedList import LinkedList

def linked_list_cycle(head):
    p1=head
    p2=head
    while p2 is not None or p2.next_element is not None:
        p1=p1.next_element
        p2=p2.next_element.next_element
        if p1==p2:
            return True
    return False

obj1=LinkedList()
obj1.insert_at_head(10)
obj1.insert_at_head(20)
obj1.insert_at_tail(30)
obj1.insert_at_tail(10)
obj1.print_linkedlist()
