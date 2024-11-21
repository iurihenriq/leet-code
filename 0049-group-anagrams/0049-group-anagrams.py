class Solution(object):
    def groupAnagrams(self, strs):
        map_string = {}

        for string in strs:
            count = [0] * 26
            
            for letter in string:
                count[ord(letter) - ord('a')] += 1
            
            key = tuple(count)

            if key not in map_string:
                map_string[key] = [string]
            else:
                map_string[key].append(string)

        return list(map_string.values())
