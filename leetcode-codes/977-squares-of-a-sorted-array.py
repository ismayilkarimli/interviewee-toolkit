from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        i = len(nums) - 1
        sorted_nums = [0 for num in nums]
        
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                sorted_nums[i] = nums[r]**2
                r -= 1
            else:
                sorted_nums[i] = nums[l]**2
                l += 1
            i -= 1

        return sorted_nums


solution = Solution()
print(solution.sortedSquares([-4, -1, 0, 3, 10]))
