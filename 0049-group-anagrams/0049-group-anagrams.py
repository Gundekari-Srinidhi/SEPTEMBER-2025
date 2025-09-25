class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            s="".join(sorted(i))
            if s in d:
                d[s]+=","
                d[s]+=i
            else:
                d[s]=i
        l=[]
        for k,v in d.items():
            l.append(sorted(v.split(",")))
        return l
