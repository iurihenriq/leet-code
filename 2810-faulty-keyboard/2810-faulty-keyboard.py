class Solution(object):
    def finalString(self, s):
        result = ''
        for letter in s:
            if letter == 'i':
                result = result[::-1]
            else:
                result += letter
        return result
        