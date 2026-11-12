class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for tick in range(k):
            index = gifts.index(max(gifts))
            gifts[index] = int(gifts[index] ** 0.5)
        
        return sum(gifts)
