class Solution(object):
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        valid_words = []
        
        for word in words:
            lower_word = set(word.lower())
            print(lower_word)
            if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
                valid_words.append(word) 

        return valid_words
