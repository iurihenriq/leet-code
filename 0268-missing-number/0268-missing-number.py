class Solution(object):
    def missingNumber(self, nums):
        sum = 0
        for i in range(0, len(nums)+1):
            sum += i
        
        for num in nums:
            sum -= num

        return sum