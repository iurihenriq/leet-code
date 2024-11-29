class Solution(object):
    def minimumLines(self, stockPrices):
        stockPrices.sort(key=lambda x: x[0])
        lines = len(stockPrices) - 1
        
        for i in range(2, len(stockPrices)):
            x1, y1 = stockPrices[i - 2]
            x2, y2 = stockPrices[i - 1]
            x3, y3 = stockPrices[i]
            
            if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
                lines -= 1
        
        return lines
