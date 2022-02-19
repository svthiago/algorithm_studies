class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nmin = prices[0]
        nmax = nmin
        profit = 0
        
        niter = len(prices)
        for i in range(1, niter):
            p = prices[i]
            
            if p < nmin:
                nmin = p
                nmax = nmin
            elif p > nmax:
                nmax = p
                if (nmax - nmin) > profit:
                    profit = nmax - nmin
        return profit
