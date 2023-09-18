from Arrays.buy_sell_stock import BuySellSock
from Arrays.product_of_array_except_self import ProductOfArrayExceptSelf
from Graphs.number_of_islands import NumberOfIslands
from Matrix.matrix import SpiralMatrix

def main():
    '''
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    island = NumberOfIslands()
    island.num_is_islands(grid)
    '''

    spr_matrix = SpiralMatrix()

    print(spr_matrix.generate_matrix(3))


if __name__ == "__main__":
    main()