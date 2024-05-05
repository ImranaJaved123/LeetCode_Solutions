class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1 
        Comp=0 
        Sort=1
        while i in range(len(nums)):
            if nums[i]==nums[Comp]:
                Comp+=1
                i+=1
            else:
                nums[Sort]=nums[i]
                Sort+=1
                i+=1
                Comp+=1
        while Sort in range(len(nums)):
            nums.pop()
