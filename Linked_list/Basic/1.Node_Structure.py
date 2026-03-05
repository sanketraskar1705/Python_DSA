"""
Linked-Lists :-
A Linked List is, as the word implies, a list where the nodes are linked together. Each node contains data and a pointer.
The way they are linked together is that each node points to where in the memory the next node is placed.
"""

# Node Structure :-
"""
Each node contains:
data
next (reference to next node)
"""
# Syntax Of Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

Node1 = Node(5)
Node2 = Node(23)
Node3 = Node(54)
Node4 = Node(13)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

print(Node1)            # output is address
print(Node2)            # output is address

print(Node1.data)       # output is 5 which is Node1 data
print(Node2.data)       # output is 23 which is Node2 data

print(Node1.next)       # Prints the reference (memory address) of the next node after Node1
print(Node2.next)       # Prints the reference (memory address) of the next node after Node2

print(Node1.next.data)  # Access the next node of Node1 and print its data value
print(Node2.next.data)  # Access the next node of Node2 and Print its data value

print(Node1.next.next.next.data) # Access the next 3 node of Node1 and print its data value