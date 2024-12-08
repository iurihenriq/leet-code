class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []

        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        for num in set_nums1:
            if num in set_nums2:
                result.append(num)

        return result