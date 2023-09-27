from Search.k_closest_point import KClosestPoint
from random_problem import chose_random

def main():
   closest = KClosestPoint()
   res = closest.kClosest([[1,2], [2,4], [4,5], [4,2], [2,1], [5,1]], 3)
   print(res)

if __name__ == "__main__":
    main()
