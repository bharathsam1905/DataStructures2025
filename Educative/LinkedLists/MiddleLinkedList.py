from SinglyLinkedList import LinkedList

def find_mid(head):
    length=0
    mid=0
    current=head
    while current is not None:
        length+=1
        current=current.next_element
        mid=length//2
    counter=0
    current=head
    while current is not None:
        if counter==mid:
            return current
        counter+=1
        current=current.next_element


obj1=LinkedList()
obj1.insert_at_head(10)
obj1.insert_at_head(20)
obj1.insert_at_tail(30)
obj1.insert_at_tail(40)
obj1.insert_at_tail(50)
obj1.insert_at_tail(70)
obj1.print_linkedlist()

obj1.mid_node=find_mid(obj1.get_head_node())

print("Middle Node")
print(obj1.mid_node.data)


