from LinkedLists.listnode import ListNode
from Recursion.merge_two_sortedLists import MergeTwoLSortedLists
from Arrays.buy_sell_stock import BuySellSock

def main():
    prices = [7,1,5,3,6,4]
    prices2 = [2,4,1]
    prices3 = [2,3,6,5,0,3]
    b = BuySellSock()
    print(b.maxProfit(prices3))
    print(float('inf'))

if __name__ == "__main__":
    main()