class Solution(object):
    def numIdenticalPairs(self, nums):
        repeat = {}
        num = 0
        
        for v in nums:
            if v in repeat:
                num += repeat[v]
                repeat[v] += 1
            else:
                repeat[v] = 1
        return num


        