class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right=0
        left=len(nums)-1
        while right<=left:
            if nums[right]!=val:
                right+=1
            elif nums[left]==val:
                nums.pop()
                left-=1
            else:
                nums[right]=nums[left]
                nums.pop()
                right+=1
                left-=1
        return len(nums)