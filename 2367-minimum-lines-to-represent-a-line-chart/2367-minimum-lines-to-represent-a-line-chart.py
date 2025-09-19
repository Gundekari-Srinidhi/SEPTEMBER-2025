class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        n=len(stockPrices)
        count=1
        if n<=1:
            return 0
        if n>1:
            for i in range(1,n-1):
                s=stockPrices[i-1]
                t=stockPrices[i]
                r=stockPrices[i+1]
                if (t[1]-s[1])*(r[0]-t[0])!=(r[1]-t[1])*(t[0]-s[0]):
                    count+=1
        return count
    

        