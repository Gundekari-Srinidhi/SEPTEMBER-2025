class Solution:
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def lcm(self,a,b):
        return (a*b)//self.gcd(a,b)
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            curr=nums[i]
            for j in range(i,n):
                curr=self.lcm(curr,nums[j])
                if curr==k:
                    count+=1
                elif curr>k:
                    break
        return count
        