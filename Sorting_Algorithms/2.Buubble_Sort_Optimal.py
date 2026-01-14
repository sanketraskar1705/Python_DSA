# Bubble Sort

# Optimal Solution
# Time Complexity is O(n)

class Solution:
    def bubble(self,arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]= arr[j+1],arr[j]
                    swapped = True

            if not swapped:
                break

        return arr

s1=Solution()
print(s1.bubble([13,1,27,4,23,65,45,51]))

"""
        1. Start

        2. Take the input array

        3. Repeat for i = 0 to n-1
              a. Set a flag `swapped = False`

              b. Repeat for j = 0 to n-i-2
                    i. Compare arr[j] and arr[j+1]
                   ii. If arr[j] > arr[j+1]
                         • Swap the two elements
                         • Set swapped = True

              c. If swapped == False
                    • Array is already sorted
                    • Stop the algorithm

        4. End


Best case: O(n)

Worst case: O(n²)

Space: O(1) 

"""