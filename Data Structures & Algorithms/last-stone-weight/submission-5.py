import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[]
        for x in stones:
            max_heap.append(-x)
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, x - y)
        if not max_heap:
            return 0
        return abs(max_heap[0])