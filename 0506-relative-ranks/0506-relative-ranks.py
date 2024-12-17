class Solution(object):
    def findRelativeRanks(self, score):
        list_score = score[:]
        list_score.sort(reverse = True)
        map_score = defaultdict(int)

        for i in range(len(list_score)):
            if i == 0:
                map_score[list_score[i]] = "Gold Medal"
            elif i == 1:
                map_score[list_score[i]] = "Silver Medal"
            elif i == 2:
                map_score[list_score[i]] = "Bronze Medal"
            else:
                map_score[list_score[i]] = str(i + 1)

        result = []
        for s in score:
            result.append(map_score[s])

        return result