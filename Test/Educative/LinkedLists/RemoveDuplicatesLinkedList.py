from SinglyLinkedList import LinkedList
def remove_duplicates(head):
    curr=head
    while curr:
        runner=curr
        while runner.next_element is not None:
            if runner.next_element.data==curr.data:
                runner.next_element=runner.next_element.next_element
            else:
                runner=runner.next_element
        curr=curr.next_element
    return head

obj1=LinkedList()
obj1.insert_at_head(10)
obj1.insert_at_head(20)
obj1.insert_at_tail(10)
obj1.insert_at_tail(40)
obj1.insert_at_tail(50)
obj1.insert_at_tail(70)
obj1.print_linkedlist()

obj1.rd=remove_duplicates(obj1.get_head_node())

obj1.print_linkedlist()

