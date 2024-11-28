class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last_interval = result[-1]

            if intervals[i][0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result
