class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(words)

        heap = [(-cnt,key) for key,cnt in count.items()]
        heapify(heap)

        arr = []
        for _ in range(k):

            arr.append(heappop(heap)[1])
        
        return arr