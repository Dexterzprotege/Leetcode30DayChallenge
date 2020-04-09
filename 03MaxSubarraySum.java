//Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

//Example:
//Input: [-2,1,-3,4,-1,2,1,-5,4],
//Output: 6
//Explanation: [4,-1,2,1] has the largest sum = 6.
//Follow up:

//If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

//Kadane's Algorithm       
public int maxSubArray(int[] nums) {
    int max_so_far = Integer.MIN_VALUE;
    int max_ending_here = 0;
    int size = nums.length;
    for(int i=0;i<size;i++){ 
        max_ending_here = max_ending_here + nums[i]; 
        if(max_so_far < max_ending_here)
            max_so_far = max_ending_here;
        if(max_ending_here < 0) 
            max_ending_here = 0;
    }
    return max_so_far 
}

//Divide and Conquer Solution
class Solution {
    static int maxCrossingSum(int arr[], int l, int m, int h) {  
        int sum = 0; 
        int left_sum = Integer.MIN_VALUE; 
        for (int i = m; i >= l; i--) { 
            sum = sum + arr[i]; 
            if (sum > left_sum) 
            left_sum = sum; 
        } 
        sum = 0; 
        int right_sum = Integer.MIN_VALUE; 
        for (int i = m + 1; i <= h; i++) { 
            sum = sum + arr[i]; 
            if (sum > right_sum) 
            right_sum = sum; 
        } 
        return left_sum + right_sum; 
    } 
    static int maxSubArraySum(int arr[], int l,   int h) { 
        if (l == h) 
            return arr[l]; 
        int m = (l + h)/2; 
        int left = maxSubArraySum(arr, l, m);
        int right = maxSubArraySum(arr, m+1, h);
        int cross = maxCrossingSum(arr, l, m, h);
        return Math.max(Math.max(left, right), cross); 
    } 
    public int maxSubArray(int[] nums) {
        return maxSubArraySum(nums, 0, nums.length-1);
    }
}
