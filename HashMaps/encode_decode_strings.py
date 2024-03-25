from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded


    def decode(self, s:str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            start = s.find('#', i)
            slen = int(s[i:start])
            decoded.append(s[start+1:start+1+slen]) 
            i = start + 1 + slen

        return decoded


