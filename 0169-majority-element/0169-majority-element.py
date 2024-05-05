class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        unique=set(nums)
        majority=len(nums)/2
        for num in unique:
            for elem in nums:
                if elem==num:
                    count+=1
            if count>majority:
                return num
            
        