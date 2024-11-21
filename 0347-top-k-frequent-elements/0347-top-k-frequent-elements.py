class Solution(object):
    def topKFrequent(self, nums, k):
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]
