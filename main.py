from LinkedLists.listnode import ListNode
from Recursion.merge_two_sortedLists import MergeTwoLSortedLists
from Arrays.buy_sell_stock import BuySellSock
from Arrays.longest_common_prefix import LongestPrefix
from Arrays.longest_common_substring import LongestCommonSubstring
from Graphs.rotate_image import RotateImage

def main():
    test_matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rot_img = RotateImage()
    # rot_img.rotate_alt(test_matrix)
    rot_img.rotate(test_matrix)

    print(test_matrix)

if __name__ == "__main__":
    main()