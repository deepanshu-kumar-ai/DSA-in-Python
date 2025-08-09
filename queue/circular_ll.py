class circularqueue:
    def __init__(self,capacity):
        self.queue=[None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rare = -1
        self.size = 0
    
    def enqueue(self,data):
        if self.isfull():
            return "the the queue is full"
        else:
            self.rare =(self.rare + 1) % self.capacity
            self.queue[self.rare]=data
            self.size = self.size + 1

    def dequeue(self):
        if self.isempty():
            return "the the queue is empty"
        remove = self.queue[self.front]
        self.queue[self.front]= None
        self.front =(self.front + 1) % self.capacity
        self.size = self.size - 1
        return remove
    
    def peek(self):
        if self.isempty():
            return "the the queue is empty"
        return self.queue[self.front]
    
    def isfull(self):
        return self.size == self.capacity
 
    def isempty(self):
        return self.size == 0
    
    def display(self):
        print("Queue:",self.queue)

cq = circularqueue(5)

print(cq.enqueue(10))
print(cq.enqueue(20))
print(cq.enqueue(30))
print(cq.enqueue(40))
print(cq.enqueue(50))
print(cq.enqueue(60))  # Should say queue is full

print("Dequeued:", cq.dequeue())      # Should remove 10
print("Peek:", cq.peek())            # Should show 20

print(cq.enqueue(60))                # Should now add 60 at front space
cq.display()                         # See current queue state
