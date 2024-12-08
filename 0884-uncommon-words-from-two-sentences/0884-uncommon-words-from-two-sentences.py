class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        words = s1 + " " + s2
        list_words = words.split(words)
        count_words = Counter(list_words)
        
        for word in count_words:
            if count_words(word) == 1:
                result.append(word)

        return result

        

        