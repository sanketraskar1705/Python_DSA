class Solution:
    def merge_sort(self, arr, low, high):
        if low >= high:
            return arrsll

        mid = (low + high) // 2

        self.merge_sort(arr, low, mid)
        self.merge_sort(arr, mid + 1, high)

        self.merge(arr, low, mid, high)

    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

arr = [5, 2, 9, 1, 3, 7, 2, 4]
s1 = Solution()
s1.merge_sort(arr, 0, len(arr) - 1)
print(arr)

