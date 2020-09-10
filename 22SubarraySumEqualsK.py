'''Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
 
Constraints:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = dict()
        d[0] = 1
        cnt = 0
        curr_sum = 0
        for i in range(0, len(nums)):
            curr_sum += nums[i]
            if curr_sum - k in d:
                cnt += d[curr_sum-k]
            d[curr_sum] = d.get(curr_sum, 0) + 1
        return cnt
