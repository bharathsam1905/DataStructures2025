def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Create the generator
'''numbers = count_up_to(5)
a='Generator' 
#print(next(numbers))
# Iterate through the generator
for num in numbers:
    print(num,a)'''

def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    
    # TODO: Write your function to reverse linked lists here

    for item in linked_list[::-1]:
        self.head=Node(item(0))
        
    print(self.head)
    
print(reverse([5,3,6,1])