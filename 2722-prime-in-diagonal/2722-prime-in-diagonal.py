class Solution:
    def prime(self,num):
        count=0
        if num==1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                count+=1
        return count==0
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n=len(nums)
        l=[]
        for i in range(n):
            s=nums[i][i]
            r=nums[i][n-i-1]
            if self.prime(s):
                l.append(s)
            if self.prime(r):
                l.append(r)
        if len(l)>0:
            return max(l)
        else:
            return 0
        