class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        n = len(nums)
        
        for i in range(0, n):
            result = target - nums[i]
            if result in d:
                return [d[result], i]
            d[nums[i]] = i
        return []