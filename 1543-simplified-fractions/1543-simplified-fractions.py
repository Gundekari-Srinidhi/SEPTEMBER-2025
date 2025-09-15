class Solution:
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def simplifiedFractions(self, n: int) -> List[str]:
        flag=1
        l=[]
        while(flag<n):
            for i in range(2,n+1):
                t=self.gcd(flag,i)
                num=flag//t
                den=i//t
                r=num/den
                if r<1 and r>0:
                    s=str(num)+"/"+str(den)
                    l.append(s)
            flag+=1
        return list(set(l))
        