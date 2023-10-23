class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        for i in range(len(piles)//3):
            sum += piles[-2-2*i]
        return sum

