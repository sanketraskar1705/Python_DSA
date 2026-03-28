# Problem :- Reverse Linked List
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
    def reverseList(self,head):
        prev=None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

s1 = Solution()

new_head = s1.reverseList(n1)

# Traverse and print
temp = new_head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next


"""
Step 1: Node Logic
A Node represents one element in a linked list.
Each node contains two parts:
1. data → stores the value of the node
2. next → stores the reference to the next node in the list

When a node is created, the next pointer is initially set to None
because the node is not yet connected to another node.


Step 2: Creating the Linked List
Five nodes are created with values:
10, 20, 30, 40, and 50.

These nodes are connected using the next pointer to form
the linked list:

10 → 20 → 30 → 40 → 50

The first node (10) acts as the head of the linked list
and traversal always starts from this node.


Step 3: Reverse Linked List Logic
The goal is to reverse the direction of the linked list.

Original direction:
10 → 20 → 30 → 40 → 50

After reversing:
50 → 40 → 30 → 20 → 10

To achieve this, three pointers are used:
1. prev → keeps track of the previous node
2. curr → keeps track of the current node
3. next_node → temporarily stores the next node


Step 4: Reversing Process
Steps performed during traversal:

1. Start with prev as None and curr pointing to the head node.
2. Store the next node of the current node in a temporary variable.
3. Change the current node’s next pointer so it points to the previous node.
4. Move the prev pointer one step forward to the current node.
5. Move the curr pointer to the next node stored earlier.
6. Repeat this process until the current pointer becomes None.

At the end of the traversal, prev will point to the new head
of the reversed linked list.


Step 5: Final Result
After reversing, the linked list becomes:

50 → 40 → 30 → 20 → 10

This reversed list is then traversed and printed.
"""
