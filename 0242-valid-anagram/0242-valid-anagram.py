class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}

        for letter in s:
            if letter in map_s:
                map_s[letter] += 1
            else:
                map_s[letter] = 1

        for letter in t:
            if letter in map_t:
                map_t[letter] += 1
            else:
                map_t[letter] = 1

        return map_t == map_s
        