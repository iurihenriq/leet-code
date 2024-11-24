class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_ = 0

        while l < r:
            m = min(height[l],height[r])*abs(l-r)
            if m > max_:
                max_ = m

            if height[l] < height[r]:
                l +=1
            else:
                r -= 1
        return max_
        