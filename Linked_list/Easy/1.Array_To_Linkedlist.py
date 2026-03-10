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