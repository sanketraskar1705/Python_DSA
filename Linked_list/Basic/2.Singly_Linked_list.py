"""
Singly Linked List (Python)

A Singly Linked List is a linear data structure where:
Each element is called a node
Each node contains:
data
next (reference to next node)
The last node points to None
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traverse(self):
        if self.head is None:
            print("SLL is empty")
        else:
            curr =self.head
            while curr is not None:
                print(curr.data,end=" ")
                curr = curr.next
            print()

    def insert(self,data,position):
        new_node = Node(data)
        if position == 0:
            new_node.next =self.head
            self.head = new_node
        else:
            current =self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count +=1
                prev_node.next = new_node
                new_node.next = current

    def delete(self,data):
        temp =self.head
        if temp.next is not None:
            if temp.data == data:
                self.head = temp.next
                return
        else:
            found = False
            prev_node = None
            while temp is not None:
                if temp.data ==  data:
                    found = True
                    break
                prev_node = temp
                temp = temp.next
            if found:
                prev_node.next = temp.next
                return
            else:
                print("Node Not Found")

























sll = SinglyLinkedList()
sll.append(23)
sll.append(12)
sll.append(56)
sll.append(2)
sll.insert(1,0)
sll.traverse()
