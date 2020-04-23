/*Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.*/
class Solution {
    public int findMaxLength(int[] nums) {
        if(nums.length<=1)
            return 0;
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for(int i=0;i<nums.length;i++)
            if(nums[i]==0)
                nums[i]=-1;
        for(int i=1;i<nums.length;i++)
            nums[i] += nums[i-1];
        int max_len = 0;
        hm.put(nums[0], 0);
        for(int i=1;i<nums.length;i++){
            if(nums[i] == 0)
                max_len = i+1;
            if(hm.containsKey(nums[i])){
                max_len = Math.max(max_len, i-hm.get(nums[i]));
            }
            else{
                hm.put(nums[i], i);
            }
        }
        return max_len;
    }
}
