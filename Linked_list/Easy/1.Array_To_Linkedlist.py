# Problem:- Array to Linked-list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def arrayToLinkedlist(self, arr):
        if not arr:
            return None

        head = Node(arr[0])
        curr = head

        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            curr.next = new_node
            curr = new_node

        return head


    def listToString(self, head):
        result = ""
        temp = head

        while temp:
            result += str(temp.data)
            if temp.next:
                result += "->"
            temp = temp.next

        return result


s1 = Solution()
arr = [1,2,3,4,5]

head = s1.arrayToLinkedlist(arr)

print(s1.listToString(head))


"""
Step 1: Node Logic
A Node represents a single element in a linked list.
Each node contains two parts:
1. data → stores the value
2. next → stores the reference to the next node

Initially, the next pointer is set to None because the node is not
connected to any other node when it is created.


Step 2: Solution Class Logic
The Solution class groups together the operations that will be
performed on the linked list, such as converting an array into
a linked list and displaying the linked list.


Step 3: Array to Linked List Conversion Logic
1. First check whether the array is empty.
   If the array is empty, return None because no linked list can be created.

2. Create the first node using the first element of the array.
   This node becomes the head of the linked list.

3. Create a pointer called curr that points to the head node.
   This pointer will help connect new nodes.

4. Traverse the array from the second element to the last element.

5. For every element in the array:
   - Create a new node with that value.
   - Connect the current node's next pointer to the new node.
   - Move the curr pointer to the new node.

6. After all elements are processed, return the head node,
   which represents the starting point of the linked list.


Step 4: Linked List to String Logic
1. Start traversal from the head node.

2. Create an empty string to store the result.

3. Use a temporary pointer to move through the linked list.

4. For every node visited:
   - Add the node's data to the string.
   - If another node exists after it, add "->" to show the connection.

5. Move the pointer to the next node and repeat the process.

6. Continue until the pointer becomes None,
   which means the end of the linked list is reached.

7. Finally return the complete string representation of the linked list.


Step 5: Main Execution Logic
1. Create an object of the Solution class.
2. Define an array containing values.
3. Convert the array into a linked list.
4. Print the linked list in a readable format.

Final Output Representation:
1->2->3->4->5
"""