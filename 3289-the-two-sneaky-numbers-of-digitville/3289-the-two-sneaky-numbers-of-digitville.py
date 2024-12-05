class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        temp = []

        for num in nums:
            if num in temp:
                result.append(num)
            else:
                temp.append(num)
        
        return result