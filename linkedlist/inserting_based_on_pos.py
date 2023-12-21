class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.first = None
        
    def insert(self, pos, val):
        temp = Node(val)
        if pos == 0:
            temp.next = self.first
            self.first = temp
        elif pos > 0:
            p = self.first
            for i in range(0, pos-1):
                if p:
                    p = p.next
            temp.next = p.next
            p.next = temp
            
    
    def display(self):
        temp = self.first
        while temp:
            print(temp.data)
            temp = temp.next
        
        
        
linked_list = LinkedList()
linked_list.insert(0, 1)
linked_list.insert(1, 2)
linked_list.insert(2, 3)
linked_list.insert(1, 5)

linked_list.display()
