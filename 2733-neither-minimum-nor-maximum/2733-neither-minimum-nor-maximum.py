class Solution(object):
    def findNonMinOrMax(self, nums):
        if len(nums) < 3:
            return -1
        
        num_min, num_max = min(nums), max(nums)
        
        for num in nums:
            if num != num_min and num != num_max:
                return num
