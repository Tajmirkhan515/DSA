
class Queue:
    def __init__(self,capacity=5):
        self.capacity=capacity
        self.items=[None]*capacity
        self.front=0
        self.rear=0
        self.size=0
        
    
    def enqueue(self,item):
        if self.size==self.capacity:
            print("Queue is full")
            return " "
        
        self.items[self.rear]=item
        self.rear+=1
        print("rear, ", self.rear)
        
        if self.rear==self.capacity:
            self.rear=0
        print("rear, ", self.rear)
        self.size+=1
        
    
    def dequeue(self):
        
        if self.is_empty():
            print(" Dequeue from an empty queue")
            return " "
        
        item=self.items[self.front]
        self.items[self.front]=None
        self.front+=1
        
        if self.front ==self.capacity:
            self.front=0
        
        self.size -=1
        return item
        
    def is_empty(self):
            return self.size == 0
    
    def peek(self):
        
        if self.is_empty():
            print( "peek from empty queue")
            return " "
        
        return self.items[self.front]
    
    
    def __len__(self):
        return self.size
        
    
    def __str__(self):
        strq=" "
        for t in self.items:
            strq+=str(t)+", "
        
        return strq



queue = Queue(5)  # Create a queue with capacity 5

#queue.enqueue(1)
#queue.enqueue(2)
#queue.enqueue(3)
print(queue)  # Output: Queue: [1, 2, 3]

print("Dequeued:", queue.dequeue())  
print("Peek:", queue.peek())         
print("Is empty?", queue.is_empty()) 

queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(5)
queue.enqueue(5)
print(queue)  # Output: Queue: [2, 3, 4, 5]
 
