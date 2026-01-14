# Insertion Sort

# Optimal Solution

class Solution:
    def insertionSort(self,arr):
        n = len(arr)
        for i in range(1,n):
            key = arr[i]
            j = i -1

            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = key

        return arr

s1=Solution()
print(s1.insertionSort([5,41,13,62,1]))























"""
1. Assume the first element of the array is already sorted.

2. Start from the second element and pick it as the current element (key).

3. Compare the key with elements in the sorted part (left side).

4. If any element is greater than the key:
      → shift that element one position to the right.

5. Continue shifting until:
      → you find a smaller element, or
      → you reach the beginning of the array.

6. Insert the key at its correct position.

7. Repeat the process for all remaining elements.

8. After all passes, the array becomes fully sorted.


"""