class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n
        left[0] = nums[0]
        right[n-1] = nums[n-1]
        for i in range(1, n):
            left[i] = left[i-1] * nums[i]
            right[n-i-1] = right[n-i] * nums[n-i-1]
        res = [1]*n
        for i in range(n):
            left_num = 1
            right_num = 1
            if i-1>=0:
                left_num = left[i-1]
            if i+1<n:
                right_num = right[i+1]
            res[i] = left_num*right_num
        return res