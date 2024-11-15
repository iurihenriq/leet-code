class Solution(object):
    def scoreOfString(self, s):
        soma = 0
        for i in range(len(s) - 1):
            soma += abs(ord(s[i]) - ord(s[i + 1]))
        return soma

        