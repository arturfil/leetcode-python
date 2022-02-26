from LinkedLists.listnode import ListNode
from Recursion.merge_two_sortedLists import MergeTwoLSortedLists
from Arrays.buy_sell_stock import BuySellSock
from Arrays.longest_common_prefix import LongestPrefix

def main():
    test = ["flower", "florida", "flight"]
    test2 = ["dog", "racecar", "car"]
    test3 = ["twenty one", "two"]
    lng = LongestPrefix()
    print(lng.longestCommonPrefix(test))

if __name__ == "__main__":
    main()