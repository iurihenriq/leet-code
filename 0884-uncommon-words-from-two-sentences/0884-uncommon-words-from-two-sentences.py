class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        list_words = (s1 + " " + s2).split(" ")
        count_words = Counter(list_words)
        result = []

        for word in count_words:
            if count_words[word] == 1:
                result.append(word)

        return result

        

        