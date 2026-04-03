# Problem:- Linked List Cycle
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""
"""
Input: head = [3,2,0,-4], pos = 1
Output: true
"""
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
n5.next=n3

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

s1=Solution()
print(s1.hasCycle(n1))


"""
Step 1: Node Logic
A Node represents a single element in a linked list.
Each node contains two parts:
1. data → stores the value of the node
2. next → stores the reference to the next node

When a node is created, the next pointer is initially set to None
because it is not connected to any other node.


Step 2: Creating the Linked List
Five nodes are created with values:
10, 20, 30, 40, and 50.

These nodes are connected using the next pointer to form
the linked list.

Normally the structure would be:
10 → 20 → 30 → 40 → 50

However, in this case a cycle is intentionally created.

The last node (50) is connected back to the node containing 30.
So the structure becomes:

10 → 20 → 30 → 40 → 50
           ↑         ↓
           ← ← ← ← ← ←

This means the list will keep looping from 50 back to 30.


Step 3: Cycle Detection Logic (Floyd’s Cycle Detection Algorithm)
To detect a cycle, two pointers are used:
1. slow pointer
2. fast pointer

Steps:
1. Both slow and fast pointers start from the head node.
2. The slow pointer moves one step at a time.
3. The fast pointer moves two steps at a time.
4. Continue moving both pointers through the linked list.


Step 4: Detecting the Cycle
If the linked list contains a cycle:
- The fast pointer will eventually catch up to the slow pointer.
- When both pointers meet at the same node, a cycle is detected.

If the fast pointer reaches the end of the list (None),
then there is no cycle in the linked list.


Step 5: Result
If the slow and fast pointers meet → return True (cycle exists)

If the traversal ends without pointers meeting → return False


Example:
Linked List:
10 → 20 → 30 → 40 → 50
           ↑         ↓
           ← ← ← ← ← ←

Result:
True (because the list forms a loop)
"""