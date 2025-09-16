class Solution:
    def primefact(self,n):
        fact=0
        d=2
        while d*d <=n:
            while n%d==0:
                fact+=d
                n//=d
            d+=1
        if n>1:
            fact+=n
        return fact
    def prime(self,n):
        while True:
            if self.primefact(n)==n:
                return n
            n=self.primefact(n)
    def smallestValue(self, n: int) -> int:
        return self.prime(n)


        