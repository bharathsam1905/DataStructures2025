from SinglyLinkedList import LinkedList

def reverse_linked_list(head):
    prev=None
    curr=head
    while curr:
        nxt=curr.next_element
        curr.next_element=prev
        prev=curr
        curr=nxt
    return prev

obj1=LinkedList()
obj1.insert_at_head(10)
obj1.insert_at_head(20)
obj1.insert_at_tail(30)
obj1.print_linkedlist()
print(obj1.search(40))
#obj1.delete(20)
#obj1.print_linkedlist()

obj1.head_node=reverse_linked_list(obj1.get_head_node())

print("Reversed list:")
obj1.print_linkedlist()


