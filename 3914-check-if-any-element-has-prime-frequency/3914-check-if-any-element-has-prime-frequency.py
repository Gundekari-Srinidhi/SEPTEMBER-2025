class Solution:
    def prime(self,n):
        count=0
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                count+=1
        return count==0
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if v>1:
                r=self.prime(v)
                if r:
                    return True
        return False
        