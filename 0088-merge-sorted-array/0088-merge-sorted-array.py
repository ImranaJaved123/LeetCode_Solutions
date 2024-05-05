class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Last index num1
        Last = m+n-1
        # merge in reverse order
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[Last]=nums1[m-1]
                m-=1
            else:
                nums1[Last]=nums2[n-1]
                n-=1
            Last-=1
        # fill with leftover elements of nums2        
        while n>0:
            nums1[Last]=nums2[n-1]
            n-=1
            Last-=1


            

        