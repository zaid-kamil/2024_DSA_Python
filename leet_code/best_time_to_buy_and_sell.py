from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 10**4 # 0 <= prices[i] <= 10^4
        for idx, value in enumerate(prices):
            if value < minPrice:
                minPrice = value
            else:
                maxProfit = max(maxProfit, value - minPrice)
        return maxProfit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))  # Output: 5

    