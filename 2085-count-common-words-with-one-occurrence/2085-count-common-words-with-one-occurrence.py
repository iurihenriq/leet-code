class Solution(object):
    def countWords(self, words1, words2):
        count_w1 = Counter(words1)
        count_w2 = Counter(words2)

        result = []

        for word in count_w1:
            if count_w1[word] == 1 and count_w2[word] == 1:
                result.append(word)

        return len(result)
        
                

        