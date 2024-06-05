from collections import deque
"""deque is a doubly linked list"""

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, var):
        self.stack.append(var)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def is_balanced(given_string):
    stack = Stack()
    parenthesis_map = {')': '(', '}': '{', ']': '['}
    for char in given_string:
        if char in parenthesis_map:  # check if closing parenthesis in hashmap
            if stack and stack.peek() == parenthesis_map[char]:  # check if stack is empty and the last value of the stack is open parenthesis
                stack.pop()
            else:
                return False
        else:
            stack.push(char)  # if opening parenthesis, add to stack
    return stack.is_empty()  # return True if stack is empty


print(is_balanced("(]"))
print(is_balanced("()[]{}"))











