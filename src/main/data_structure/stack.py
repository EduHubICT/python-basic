class Stack:

    # Constructor to initiate stack
    def __init__(self, stack=None):
        if stack is None:
            stack = []
        self.stack = stack

    # this returns the top item of stack
    def top(self):
        if Stack.empty(self) is False:
            return self.stack[-1]
        else:
            print("An empty stack")

    # pop to remove an item from stack
    def pop(self):
        if Stack.empty(self) is False:
            self.stack.pop(-1)
        else:
            print("An empty stack")

    # push to append an item in stack
    def push(self, value):
        self.stack.append(value)

    # to check stack is empty or not
    # to verify any invalid actions
    def empty(self):
        if Stack.size(self) <= 0:
            return True
        else:
            return False

    # to check stack size
    def size(self):
        return len(self.stack)

    # to see elements of stack
    def show(self):
        print(self.stack)
