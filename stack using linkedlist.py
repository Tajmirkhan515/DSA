class Node:
    def __init__(self,value):
        self.data=value
        self.Next=None

class Stack:
    def __init__(self):
        self.top=None
    
    def isEmpty(self):
        return self.top is None
    
    def push(self, value):
        new_node=Node(value)
        new_node.Next=self.top
        self.top=new_node
        print("pushed: ", value)
    
    def pop(self):
        
        if self.isEmpty():
            print(" Underflow")
            return None
        
        ppdata=self.top.data
        self.top=self.top.Next
        return ppdata
    
    def peek(self):
        if self.isEmpty():
            print("Stack empty nothing in the top")
            return None
        return self.top.data
    
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        
        current = self.top
        print("Stack elements (top to bottom):")
        while current:
            print(current.data)
            current = current.Next
        print("None")
            
        
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Top element is:", stack.peek())
stack.pop()
stack.display()
        
        
        
        
        
        
        
        
        
        

