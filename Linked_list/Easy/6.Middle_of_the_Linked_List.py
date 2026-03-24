# Problem:- Middle of the Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

class Solution:
    def middleNode(self,head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

s1=Solution()
middle = s1.middleNode(n1)
print(middle.data)

"""
Step 1: Node Logic
A Node represents a single element in a linked list.
Each node contains two components:
1. data → stores the value of the node
2. next → stores the reference to the next node in the list

When a node is created, the next pointer is initially set to None
because it is not connected to another node yet.


Step 2: Creating the Linked List
Five nodes are created with values:
10, 20, 30, 40, and 50.

These nodes are connected using the next pointer to form
the following linked list:

10 → 20 → 30 → 40 → 50

The first node (10) acts as the head of the linked list,
which is the starting point for traversal.


Step 3: Middle Node Logic (Slow and Fast Pointer Technique)
The goal is to find the middle node of the linked list efficiently.

Two pointers are used:
1. slow pointer
2. fast pointer

Steps:
1. Both slow and fast pointers start from the head node.
2. The slow pointer moves one step at a time.
3. The fast pointer moves two steps at a time.
4. Continue moving both pointers until the fast pointer
   reaches the end of the linked list.

Because the fast pointer moves twice as fast,
when it reaches the end of the list, the slow pointer
will be exactly at the middle node.


Step 4: Returning the Middle Node
Once the loop stops, the slow pointer will point to
the middle node of the linked list.

Return this node as the result.


Step 5: Example Result
Linked List:
10 → 20 → 30 → 40 → 50

The middle element is:
30

Output:
30
"""