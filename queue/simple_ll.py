class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

head = None  # front of queue
q = None     # rear of queue

def enqueue():
    global head, q
    while True:
        ele = int(input("enqueue element: "))
        new_node = Node(ele)

        if head is None:
            head = q = new_node
        else:
            q.link = new_node
            q = new_node
        
        choice = input("do you wanna enqueue (y/n): ").lower()
        if choice != 'y':
            break

def dequeue():
    global head, q
    if isempty():
        print("The queue is empty.")
    else:
        print(f"The element {head.data} is deleted.")
        head = head.link
        if head is None:
            q = None  # reset tail too

def isempty():
    return head is None

def peek():
    if isempty():
        print("The queue is empty.")
    else:
        print(f"Front element is: {head.data}")

def display():
    if isempty():
        print("The queue is empty.")
        return
    p = head
    print("Queue: ", end="")
    while p:
        print(p.data, end=" -> ")
        p = p.link
    print("None")

enqueue()
display()
peek()
dequeue()
display()