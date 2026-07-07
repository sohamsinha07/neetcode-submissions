import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for freq, num in min_heap]

        