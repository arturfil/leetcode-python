class ValidWordAbbreviation:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, num = 0, 0
        for ch in abbr:
            if ch.isdigit():
                if num == 0 and ch == "0": # not valid to have leading zeros
                    return False
                # if it's a 12 then int(ch) + (10 * num) if num == 0 then just int(ch)
                # and you save it in num for when you finish parsing through the number
                num = int(ch) + 10 * num
            else:
                i, num = i + num, 0
                if i >= len(word) or word[i] != ch:
                    return False
                i += 1

        return i + num == len(word)
        
