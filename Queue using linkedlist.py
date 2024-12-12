class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
       
    def enqueue(self,data):
        new_node=Node(data)
        if self.front is None:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
            
        self.size+=1


    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return " "
        else:
            temp=self.front
            data=temp.data
            self.front=self.front.next
            temp.next=None
            #If the queue becomes empty, update rear to None
            if self.front is None:
                self.rear=None

            self.size-=1
            return data
        
    def is_empty(self):
        return self.size==0

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return " "
        else:
            return self.front.data
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            temp=self.front
            result=""
            while temp is not None:
                result+=str(temp.data)+" "
                temp=temp.next
            return result




lk=LinkedList()
lk.enqueue(1)
lk.enqueue(2)
lk.enqueue(3)
lk.enqueue(4)
print(lk)
print(lk.dequeue())
print(lk.dequeue())
print(lk)
print(lk.dequeue())

print(lk.dequeue())
