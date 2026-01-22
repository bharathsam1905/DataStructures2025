from SinglyLinkedList import LinkedList

# def __init__(self,data):
#     self.data=data  # Data Field
#     self.next_element=None # Pointer to the next node
def union(head1, head2):
    if head1==None:
         if head2==None:
              return None
         return head2
    current_node1=head1
    current_node2=head2
    while current_node1 is not None:
        current_node1=current_node1.next_element
    current_node1.next_element=head2
    remove_duplicates(head1)
    return head1
def remove_duplicates(head):
      if head is None:
           return
      outer_node=head
        while outer_node is not None:
          inner_node=outer_node
          while inner_node.next_element is not None:
              if outer_node.data==inner_node.next_element.data:
                  inner_node.next_element=inner_node.next_element.next_element
              else:
                    inner_node=inner_node.next_element
            
        