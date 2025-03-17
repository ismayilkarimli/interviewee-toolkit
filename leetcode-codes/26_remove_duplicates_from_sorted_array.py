from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1

        while r < len(nums):
            if nums[l] != nums[r]:
                nums[l + 1] = nums[r]
                l += 1                
            r += 1
        
        return l + 1

solution = Solution()
nums=[1, 1, 2]
print(solution.removeDuplicates(nums))
print(nums)