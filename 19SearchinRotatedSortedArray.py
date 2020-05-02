'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search (arr, l, h, key): 
            if l > h: 
                return -1
            mid = (l + h) // 2
            if arr[mid] == key: 
                return mid 
            if arr[l] <= arr[mid]: 
                if key >= arr[l] and key <= arr[mid]: 
                    return search(arr, l, mid-1, key) 
                return search(arr, mid+1, h, key) 
            if key >= arr[mid] and key <= arr[h]: 
                return search(arr, mid+1, h, key) 
            return search(arr, l, mid-1, key) 
        i = search(nums, 0, len(nums)-1, target)
        return i
