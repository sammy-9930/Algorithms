"""Create a new node.
   Add the Data
   Make temp node next to point on first.
   Change first node to newly created temp node.
   Time complexity = O(1)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end="-> ")
            current = current.next
        print("None")
        
my_linked_list = LinkedList()
my_linked_list.insert_at_beginning(10)
my_linked_list.insert_at_beginning(5)
my_linked_list.insert_at_beginning(2)

my_linked_list.display()
