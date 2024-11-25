class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            meio = (r + l) // 2
            if nums[meio] == target:
                return meio
            elif nums[meio] < target:
                l = meio + 1
            else:
                r = meio - 1
        return l
