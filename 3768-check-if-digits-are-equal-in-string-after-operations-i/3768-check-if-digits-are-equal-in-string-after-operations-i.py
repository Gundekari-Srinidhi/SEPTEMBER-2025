class Solution:
    def hasSameDigits(self, s: str) -> bool:
        temp=s
        while len(temp)>2:
            n=len(temp)
            r=""
            for i in range(n-1):
                sum1=str((int(temp[i])+int(temp[i+1]))%10)
                r=r+sum1
            temp=r
        l=list(temp)
        if len(set(l))==1:
            return True
        return False



        