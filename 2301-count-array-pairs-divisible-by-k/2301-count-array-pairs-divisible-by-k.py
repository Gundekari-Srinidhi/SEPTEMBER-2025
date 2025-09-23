class Solution:
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def countPairs(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        l=[]
        d={}
        for i in nums:
            l.append(self.gcd(i,k))
        for j in l:
            if j in d:
                d[j]+=1
            else:
                d[j]=1
        g_vals=list(d.keys())
        for i in range(len(g_vals)):
            for j in range(i,len(g_vals)):
                g1,g2=g_vals[i],g_vals[j]
                if (g1*g2)%k==0:
                    if i==j:
                        count+=d[g1]*(d[g2]-1)//2
                    else:
                        count+=d[g1]*d[g2]
        return count
            
        