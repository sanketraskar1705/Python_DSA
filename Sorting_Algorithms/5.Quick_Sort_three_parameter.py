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
