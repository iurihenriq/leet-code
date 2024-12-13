class Solution(object):
    def missingNumber(self, nums):
        result = (len(nums) * (len(nums) + 1)) // 2
        
        for num in nums:
            result -= num

        return result