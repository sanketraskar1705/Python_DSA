# Problem:- Search in Linked List
"""
Given a linked list with the head node and a key, the task is to check if the key is present in the linked list or not.
Return true if key is present, else return false.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)

n1.next=n2
n2.next=n3
n3.next=n4

class Solution:
    def searchKey(self,head,data):
        curr=head
        while curr is not None:
            if curr.data == data:
                return True
            curr = curr.next
        return False

s1=Solution()

print(s1.searchKey(n1,30))


"""
Step 1: Node Logic
A Node represents a single element in a linked list.
Each node contains two parts:
1. data → stores the value of the node
2. next → stores the reference to the next node

When a node is created, the next pointer is initialized as None
because it is not yet connected to another node.


Step 2: Creating the Linked List
Four nodes are created with values:
10, 20, 30, and 40.

These nodes are connected using the next pointer.

Structure of the linked list:
10 → 20 → 30 → 40

The first node (10) is the head of the linked list,
and traversal of the list always starts from the head.


Step 3: Search Operation Logic
The goal is to check whether a given key exists in the linked list.

Steps:
1. Start traversal from the head node.
2. Create a pointer that moves through the linked list.
3. At each node, compare the node's data with the given key.
4. If the values match, it means the key is present,
   so return True.
5. If they do not match, move to the next node.
6. Continue this process until the pointer becomes None.

If the traversal finishes and the key is not found,
return False.


Step 4: Result
If the key exists in the linked list, the output will be True.
If the key does not exist in the linked list, the output will be False.

Example:
Linked List: 10 → 20 → 30 → 40
Search Key: 30

Result:
True
"""