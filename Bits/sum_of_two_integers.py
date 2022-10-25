class SumOfTwoIntegers:
    def sum_of_two(self, a: int, b: int) -> int:
        # 0011 3
        # 0110 6
        # result 9
        carry = a & b
        xor = a ^ b
        tot = carry ^ xor    
        
        while carry != 0:
            carry = a & b
            xor = a ^ b
            tot = carry ^ xor
        return tot
                            