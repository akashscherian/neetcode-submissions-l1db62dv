class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i] = 1

        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:k]
        return [item[0] for item in sorted_items]                
        