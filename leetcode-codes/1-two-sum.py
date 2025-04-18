from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):            
            if num in hm:
                return [hm[num], i]
            hm[target - num] = i
        
        return [-1, -1]
            
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
