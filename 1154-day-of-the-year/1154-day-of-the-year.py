class Solution(object):
    def dayOfYear(self, date):
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = map(int, date.split("-"))
        
        is_leap = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
        if is_leap:
            months[1] = 29
        
        return sum(months[:m-1]) + d
