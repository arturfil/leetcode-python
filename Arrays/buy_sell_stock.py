from typing import List

class BuySellSock:
    def maxProfit(self, prices: List[int]) -> int:
        max_price, min_price = 0, float('inf')
        for stock in prices:
            if stock < min_price:
                min_price = stock
            else:
                max_price = max(max_price, stock - min_price)

        return max_price

'''
    TESTING
    prices = [7,1,5,3,6,4] # -> 5
    prices2 = [2,4,1] # -> 2
    prices3 = [2,3,6,5,0,3] # -> 4
    b = BuySellSock()
    print(b.maxProfit(prices3))

    EXPLANATION
    - You want to keep track of your min value
    but at the same time the max value as you go after 
    the fact you have a min value.
    - By doing if elif you will always keep track of the min
    value first and the max value after and thus,
    return max profit with the rules of buy first sell after
'''