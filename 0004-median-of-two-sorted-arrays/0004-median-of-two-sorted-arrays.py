class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        for i in range(m):
            nums1.append(nums2[i])
        res=sorted(nums1)
        l=len(res)
        if l%2!=0:
            r=l//2
            return res[r]
        else:
            r=l//2
            s=(res[r-1]+res[r])/2
            return s
            
        