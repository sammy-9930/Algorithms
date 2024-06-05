"""Write a function in python that can reverse a string using stack data structure.
reverse_string("We will conquere COVID-19") should return '91-DIVOC ereuqnoc lliw eW'"""

from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


stack = Stack()
input_string = "We will conquere COVID-19"
for char in input_string:
    stack.push(char)
output_string = ""
while not stack.is_empty():
    output_string += stack.pop()
print("output string: ", output_string)

