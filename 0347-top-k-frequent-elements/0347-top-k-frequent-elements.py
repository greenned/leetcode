class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        counter = sorted(list(counter.items()), key=lambda x: x[1])[-k:]
        return [c[0] for c in counter]

        