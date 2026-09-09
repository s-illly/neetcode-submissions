class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        d = dict()
        for i in nums:
            d[i] = d.get(i, 0) + 1
        heap = []
        for n in d.keys():
            heapq.heappush(heap, (d[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        # sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse = True))
        # return list(sorted_d.keys())[:k]