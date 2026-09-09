class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        d = dict()
        for i in nums:
            d[i] = d.get(i, 0) + 1
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse = True))
        return list(sorted_d.keys())[:k]