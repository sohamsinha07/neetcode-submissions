import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]

        #Time complexity of O(nlogk)
            #where n is the size of nums and k is k
        #space complexity is O(k)
            #created an array of upto size k