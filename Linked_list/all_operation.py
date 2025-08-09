# Write Python 3 code in th# Function to display the linked list
def dip(start):
    cunode = start
    while cunode is not None:
        print(cunode.data, end=" -> ")
        cunode = cunode.link
    print(None)
    
# Function to find the shortest value in the linked list
def short(start):
    short_val = start.data  # by default the shortest value in the LL is value of first node
    cunode = start
    while cunode is not None:
        if short_val >= cunode.data:
            short_val = cunode.data
        cunode = cunode.link
    return short_val
    
# Function to delete a node by value
def del_by_val(start, del_val):
    prev = None
    cunode = start

    while cunode is not None:
        if cunode.data == del_val:
            if prev is None:
                # Deleting the first node, update start
                start = cunode.link
            else:
                # Deleting a node after the first one
                prev.link = cunode.link

            # Delete the node
            del cunode
            print(f"Node with value {del_val} deleted.")
            return start  # Return the updated start after deletion

        prev = cunode
        cunode = cunode.link

    print(f"Value {del_val} not found in the list.")
    return start  # If not found, return the original start

#function to add a node on the beging of the node 
def ins_at_beg(start,val):
    new_node=node(val)
    new_node.link=start
    return new_node
    # dip(start)
    
#function to add an element at the end of the node 
def ins_at_end(start,val):
    new_node=node(val)
    if start==None:
        return new_node
    else:
        cunode=start
        while cunode.link is not None:
            cunode=cunode.link
        cunode.link=new_node
    return start
   
    
class node:
    def __init__(self, data):
        self.data = data
        self.link = None

#function to add the node at user position
def ins_at_pos(start, val, pos):
    new_node = node(val)  # Now using Node class
    
    if start is None:
        start = new_node
        return start  # Return after creating a new start for empty list
    
    else:
        cunode = start
        for i in range(pos - 1):  # Loop up to position - 1 (previous node)
            if cunode is None:  # If position is out of range
                break
            cunode = cunode.link
        
        if cunode is None:  # If the position is invalid, do nothing
            return start
        
        new_node.link = cunode.link  # Link the new node to the next node
        cunode.link = new_node  # Link the previous node to the new node
    
    return start  # Return the updated list head

start = None
q = None

# Adding nodes to the linked list
while True:
    ele = int(input("enter the element into the node: "))
    p = node(ele)

    if start == None:
        start = p
        q = p
    else:
        q.link = p
        q = p
    choice = input("do you wanna add one more node (y/n) :")
    if choice.lower() != 'y':
        break


# Display the entered list
dip(start)


# Calling function to find the shortest value in the LL
print("The shortest value in the LL is:", short(start))


# Calling del_by_val function to delete the node
val = int(input("Enter the value to be deleted: "))
start = del_by_val(start, val)  # Capture the updated start after deletion

# Display the updated linked list
dip(start)

#function to insert an element(node) at the begining
c=input("Do you want to add an node in the beging of the Linkd list (y/n) : ")
if c.lower() == 'y':
    val=int(input("enter the value: "))
    start=ins_at_beg(start,val)
    dip(start)
    
#function to insert an element(node) at the begining
c=input("Do you want to add an node in the end of the Linkd list (y/n) : ")
if c.lower() == 'y':
    val=int(input("enter the value: "))
start=ins_at_end(start,val)
dip(start)
    
#function to insert an element(node) at the SPECIFIC position
c=input("Do you want to add an node in the anywhrre in the middle of the Linkd list (y/n) : ")
if c.lower() == 'y':
    val=int(input("enter the value: "))
    pos=int(input("enter the position: "))
start=ins_at_pos(start, val, pos)
dip(start)