class Solution(object):
    def isSameAfterReversals(self, num):
        return not (str(num).endswith("0") and len(str(num)) > 1)
        