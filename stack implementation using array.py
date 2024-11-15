class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty stack using a list

    def push(self, value):
        self.stack.append(value)  # Adds an element to the end of the list (top of the stack)

    def pop(self):
        if not self.is_empty():  # Check if the stack is empty before popping
            return self.stack.pop()  # Removes and returns the last element (top of the stack)
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():  # Check if the stack is empty before peeking
            return self.stack[-1]  # Returns the last element without removing it
        else:
            print("Stack is empty. Cannot peek.")
            return None

    def is_empty(self):
        return len(self.stack) == 0  # Returns True if the stack is empty, otherwise False

    def size(self):
        return len(self.stack)  # Returns the number of elements in the stack

    def display(self):
        print("Stack contents:", self.stack)  # Display the stack's current contents
  

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  # Output: Stack contents: [10, 20, 30]

print("Top of the stack:", stack.peek())  # Output: Top of the stack: 30
print("Popped element:", stack.pop())    # Output: Popped element: 30
stack.display()  # Output: Stack contents: [10, 20]

print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

