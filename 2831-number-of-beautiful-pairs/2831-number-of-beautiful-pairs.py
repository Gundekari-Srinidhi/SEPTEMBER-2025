class Solution:
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def first(self,a):
        while a>=10:
            a=a//10
        return a
    def last(self,a):
        return a%10
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for i in range(n-1):
            for j in range(i+1,n):
                r=self.gcd(self.first(nums[i]),self.last(nums[j]))
                if r==1:
                    count+=1
        return count

        