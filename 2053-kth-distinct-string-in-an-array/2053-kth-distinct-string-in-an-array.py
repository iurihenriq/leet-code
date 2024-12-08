class Solution(object):
    def kthDistinct(self, arr, k):
        count_array = Counter(arr)
        count = 0

        for s in arr: 
            if count_array[s] == 1:
                count += 1
                if count == k:
                    return s

        return ""