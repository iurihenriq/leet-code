class Solution(object):
    def reverseWords(self, s):
        words = s.split()[::-1]
        result = ' '.join(word for word in words)
        return result