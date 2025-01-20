class Solution(object):
    def isAcronym(self, words, s):
        string = ""
        for word in words:
            string += word[0]
        return string == s
        