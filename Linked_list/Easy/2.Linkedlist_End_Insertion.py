# Problem:- Linkedlist End Insertion

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

# Print original list
temp = n1
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

class Solution:
    def insertAtEnd(self,head,data):
        new_node=Node(data)

        if head is None:
            return new_node

        current = head
        while current.next:
            current = current.next

        current.next = new_node

        return head

sol = Solution()
head = sol.insertAtEnd(n1, 50)

print("\nAfter Insertion:")

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next


"""
Step 1: Node Logic
A Node represents a single element in a linked list.
Each node contains two parts:
1. data → stores the value of the node
2. next → stores the reference (pointer) to the next node

Initially, the next pointer is set to None because the node
is not connected to any other node when it is created.


Step 2: Creating the Initial Linked List
Four nodes are created with values 10, 20, 30, and 40.
These nodes are then connected using the next pointer.

Connection structure:
10 → 20 → 30 → 40

The first node (10) acts as the head of the linked list,
which means traversal of the list always starts from this node.


Step 3: Printing the Original Linked List
A temporary pointer is used to traverse the linked list.

Logic:
1. Start from the head node.
2. Print the data of the current node.
3. Move the pointer to the next node.
4. Repeat the process until the pointer becomes None.

This prints the linked list in the format:
10 -> 20 -> 30 -> 40 ->


Step 4: End Insertion Logic
The goal is to insert a new node at the end of the linked list.

1. Create a new node containing the value that needs to be inserted.

2. Check if the linked list is empty.
   If the head is None, return the new node because it will
   become the first node of the list.

3. If the list is not empty, start traversal from the head node.

4. Move through the linked list until the last node is reached.
   The last node is identified when its next pointer is None.

5. Once the last node is found, connect its next pointer
   to the new node.

6. Return the head node because the start of the list
   remains unchanged.


Step 5: Printing the Linked List After Insertion
Again, a temporary pointer is used to traverse the list.

1. Start from the head node.
2. Print each node's data.
3. Move to the next node.
4. Continue until the pointer becomes None.

After inserting the new value (50), the final linked list becomes:

10 -> 20 -> 30 -> 40 -> 50 ->
"""