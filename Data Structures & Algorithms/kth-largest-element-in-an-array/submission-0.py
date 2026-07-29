class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #inefficient way to do it would be to sort the entire array
        #then to iterate through the sorted array backwards for k iterations and return the result
        #time complexity of nlogn where n is the length of the nums array

        #an efficient way to solve the problem may be to utilize a minheap
        #set a minheap with the first k elements in the array
        #if the next element is larger than an element in k, pop the smallest element
        #iterate to the end of the array
        #return the heap result

        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]