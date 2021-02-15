# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# method 0 : bfs > 	Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(0, len(prices) - 1):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] - buy > max_profit:
                    max_profit = prices[j] - buy

        return max_profit

# mehtod 1: 저점과 현재값과의 차이 계산 > 1060 ms	25.1 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit