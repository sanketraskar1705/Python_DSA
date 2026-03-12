# Problem:- Delete Node in a Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(4)
n2=Node(2)
n3=Node(7)
n4=Node(5)

n1.next=n2
n2.next=n3
n3.next=n4

# Print original list
temp = n1
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print()

class Solution:
    def deleteNode(self, node):
        node.data = node.next.data
        node.next = node.next.next

s1 = Solution()

# pass node not value
s1.deleteNode(n3)

# print updated list
temp = n1
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

"""
Step 1: Node Logic
A Node represents one element of a linked list.
Each node contains two components:
1. data → stores the value inside the node
2. next → stores the reference to the next node in the list

Initially the next pointer is set to None when the node is created.


Step 2: Creating the Linked List
Four nodes are created with values:
4, 2, 7, and 5.

These nodes are connected using the next pointer.

Structure of the linked list:
4 → 2 → 7 → 5

The first node (4) acts as the head of the linked list,
which is the starting point for traversal.


Step 3: Printing the Original Linked List
A temporary pointer is used to traverse the list.

Logic:
1. Start from the head node.
2. Print the data of the current node.
3. Move the pointer to the next node.
4. Repeat this process until the pointer becomes None.

This displays the list as:
4 -> 2 -> 7 -> 5 ->


Step 4: Delete Node Logic
In this problem, we are given the node to be deleted,
not the head of the linked list.

So instead of removing the node directly, we perform
a trick using the next node.

Steps:
1. Copy the data of the next node into the current node.
2. Change the next pointer of the current node so it skips
   the next node and points to the next-next node.

This effectively removes the next node from the list and
replaces the current node's value with it.

Example:
Original List:
4 → 2 → 7 → 5

If we delete node 7:

1. Copy data from node 5 into node 7.
2. Update the pointer to skip node 5.

Final List:
4 → 2 → 5


Step 5: Printing the Updated Linked List
After deletion, traverse the linked list again.

1. Start from the head node.
2. Print each node's data.
3. Move to the next node.
4. Continue until the pointer becomes None.

Final Output:
4 -> 2 -> 5 ->
"""