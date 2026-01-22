from SinglyLinkedList import LinkedList

# def __init__(self,data):
#     self.data=data  # Data Field
#     self.next_element=None # Pointer to the next node
def union(head1, head2):
    current_node1=head1
    current_node2=head2
    while current_node1 is not None:
        current_node1=current_node1.next_element
    current_node1.next_element=head2
    outer_node=head1
    while outer_node is not None:
        inner_node=head1
        outer_node=current_node1.next_element
        if inner_node==outer_node:
            inner_node.next_element=outer_node.next_element
            outer_node=inner_node.next_element
        
     

    