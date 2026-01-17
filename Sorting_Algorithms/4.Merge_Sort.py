class Solution:
    def merge_sort(self,arr):
        if len(arr) <=1:
            return arr

        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        left_arr =self.merge_sort(left_arr)
        right_arr = self.merge_sort(right_arr)

        return self.merge_array(left_arr,right_arr)

    def merge_array(self,left_arr,right_arr):
        result = []
        i = j = 0
        while i <len(left_arr) and j <len(right_arr):
            if left_arr[i] < right_arr[j]:
                result.append(left_arr[i])
                i += 1
            else:
                result.append(right_arr[j])
                j += 1

        result.extend(left_arr[i:])
        result.extend(right_arr[j:])
        return result


s1 = Solution()
print(s1.merge_sort([12,2,3,1,3,22,21,1]))