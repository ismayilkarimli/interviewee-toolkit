from typing import List
from collections import deque

class Solution:
      def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = len(nums) + 1
        cur_sum = 0
        q = deque() # stores (prefix_sum, end_idx)

        for r in range(len(nums)):
            cur_sum += nums[r]

            if cur_sum >= k:
                res = min(res, r + 1)
            
            # check if its possible to minimize the length of the subarray
            # the length can be minimized if prefix_sum at the start of the subarray is less than cur_sum - k/
            while q and cur_sum - q[0][0] >= k:
                _, end_idx = q.popleft()
                res = min(res, r - end_idx)
            
            # if the current prefix_sum is less than the last one in the queue, we can pop it
            # because it unnecessarily increases the length of the subarray
            while q and q[-1][0] > cur_sum:
                q.pop()
            
            q.append((cur_sum, r))
        
        return res if res <= len(nums) else -1

solution = Solution()
# print(solution.shortestSubarray([1,2], 4)) # 2
# print(solution.shortestSubarray([2,-1,2,3,4], 5)) # 2
# print(solution.shortestSubarray([1,2,3,4,5], 11)) # 3
print(solution.shortestSubarray([84,-37,32,40,95], 167)) # 3