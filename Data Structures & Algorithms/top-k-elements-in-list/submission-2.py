class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = defaultdict(int)

        for num in nums:
            mapp[num] += 1
            
        return sorted(mapp, key=mapp.get, reverse=True)[:k]
        
