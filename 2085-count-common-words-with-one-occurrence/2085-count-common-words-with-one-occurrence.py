class Solution(object):
    def countWords(self, words1, words2):
        count_w1 = Counter(words1)
        count_w2 = Counter(words2)

        aux = []
        result = 0

        for c in count_w1:
            if count_w1[i] == 1:
                aux.append(c)
        
        for c in count_w2:
            if count_w2[i] == 1:
                aux.append(c)

        for a in aux:
            if aux.count(a) = 2:
                result += 1

        return result
        
                

        