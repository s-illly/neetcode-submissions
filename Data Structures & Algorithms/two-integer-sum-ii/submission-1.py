class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set = set(numbers)
        n = len(numbers)
        for i in range(n):
            res = target - numbers[i]
            if res in num_set:
                remainder = numbers[i + 1:]
                return [i + 1, remainder.index(res) + (i + 1) + 1]
        
