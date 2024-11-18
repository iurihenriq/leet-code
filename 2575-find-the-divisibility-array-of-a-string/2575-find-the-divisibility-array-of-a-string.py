class Solution(object):
    def divisibilityArray(self, word, m):
        prefix = 0
        div = []

        for num in word:
            prefix = (prefix * 10 + int(num)) % m
            div.append(1 if prefix == 0 else 0)
        
        return div