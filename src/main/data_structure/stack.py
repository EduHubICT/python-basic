from collections import deque


class Stack:

    # Constructor to initiate stack
    def __init__(self, stack=None):
        if stack is None:
            stack = []
        self.stack = stack
        self.q1 = deque()
        self.q2 = deque()

    # this returns the top item of stack
    def top(self):
        if Stack.empty(self) is False:
            return self.stack[-1]
        else:
            raise IndexError("You are trying to top in an empty stack.")

    # pop to remove an item from stack
    def pop(self):
        if Stack.empty(self) is False:
            self.stack.pop(-1)
        else:
            raise IndexError("You are popping from in an empty stack.")

    # push to append an item in stack
    def push(self, value):
        self.stack.append(value)

    # to check stack is empty or not
    # to verify any invalid actions
    def empty(self):
        if self.size() <= 0:
            return True
        else:
            return False

    # to check stack size
    def size(self):
        return len(self.stack)

    # to see elements of stack
    def display(self):
        return self.stack
