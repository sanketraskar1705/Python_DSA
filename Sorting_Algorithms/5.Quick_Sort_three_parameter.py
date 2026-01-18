class Solution:
    def quick_sort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quick_sort(arr, low, p - 1)
            self.quick_sort(arr, p + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while i <= high and arr[i] <= pivot:
                i += 1

            while arr[j] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j


arr = [5,4,3,3,52,1]
s1 = Solution()
s1.quick_sort(arr, 0, len(arr)-1)
print(arr)


"""
Logic of Quick Sort (using Hoare-style partition):

1. Quick Sort is a divide-and-conquer algorithm.
2. Choose the first element of the array as the pivot.
3. Partition the array so that:
   - All elements smaller than or equal to the pivot are on the left side.
   - All elements greater than the pivot are on the right side.
4. Use two pointers:
   - `i` starts from the left (low index).
   - `j` starts from the right (high index).
5. Move `i` forward until an element greater than the pivot is found.
6. Move `j` backward until an element smaller than or equal to the pivot is found.
7. If `i < j`, swap the elements at `i` and `j`.
8. Repeat steps 5–7 until `i` is no longer less than `j`.
9. Swap the pivot element with the element at index `j`.
10. The pivot is now in its correct sorted position.
11. Recursively apply Quick Sort to:
    - The left subarray (low to pivot index − 1).
    - The right subarray (pivot index + 1 to high).
12. Continue recursion until subarrays have one or zero elements.
13. The array gets sorted in place without using extra memory.
"""

