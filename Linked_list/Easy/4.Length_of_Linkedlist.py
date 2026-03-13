# Problem:- Length of Linked-list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)

n1.next=n2
n2.next=n3
n3.next=n4

temp = n1
while temp:
    print(temp.data,end="->")
    temp = temp.next
print()

class Solution:
    def getCount(self,data):
        curr=data
        count=0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

s1=Solution()
print(s1.getCount(n1))


"""
Step 1: Node Logic
A Node represents one element in a linked list.
Each node has two parts:
1. data → stores the value of the node
2. next → stores the reference to the next node in the list

When a node is created, the next pointer is set to None
because it is not yet connected to another node.


Step 2: Creating the Linked List
Four nodes are created with values:
1, 2, 3, and 4.

These nodes are connected using the next pointer to form
a linked list.

Structure of the list:
1 → 2 → 3 → 4

The first node (1) acts as the head of the linked list,
which is the starting point for traversal.


Step 3: Printing the Linked List
A temporary pointer is used to traverse the linked list.

Logic:
1. Start from the head node.
2. Print the data of the current node.
3. Move the pointer to the next node.
4. Continue this process until the pointer becomes None.

Output format:
1->2->3->4->


Step 4: Length of Linked List Logic
The goal is to count how many nodes exist in the linked list.

Steps:
1. Create a pointer that starts from the head node.
2. Initialize a counter variable with value 0.
3. Traverse the linked list node by node.
4. For every node visited, increase the counter by 1.
5. Move the pointer to the next node.
6. Continue this process until the pointer becomes None.

When traversal finishes, the counter will contain
the total number of nodes in the linked list.


Step 5: Returning the Result
After the traversal ends, return the counter value.

For the linked list:
1 → 2 → 3 → 4

Total number of nodes = 4
"""