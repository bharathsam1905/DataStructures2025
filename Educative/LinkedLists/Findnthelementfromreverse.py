from SinglyLinkedList import LinkedList
# Definition for a linked list node
# class LinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


def find_nth(head, n):
    if head is None:
        return None

    # compute length
    level = 0
    temp = head
    while temp is not None:
        level += 1
        temp = temp.next_element

    if n <= 0 or n > level:
        return None

    target_index = level - n

    current_node = head
    counter = 0
    while current_node is not None and counter < target_index:
        current_node = current_node.next_element
        counter += 1

    return current_node.data if current_node else None



##Enter Data
obj1=LinkedList()
obj1.insert_at_head(10)
obj1.insert_at_head(20)
obj1.insert_at_tail(30)
obj1.insert_at_tail(10)
obj1.print_linkedlist()

##Find nth element from reverse
n=3
result=find_nth(obj1.get_head_node(),n)
print('result:',result)







    

    

    