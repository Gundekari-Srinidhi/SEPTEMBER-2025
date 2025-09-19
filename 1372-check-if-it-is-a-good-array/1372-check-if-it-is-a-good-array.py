class Solution:
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a

    def isGoodArray(self, nums: List[int]) -> bool:
        curr=nums[0]
        for i in range(1,len(nums)):
            curr=self.gcd(curr,nums[i])
            if curr==1:
                return True
        return curr==1