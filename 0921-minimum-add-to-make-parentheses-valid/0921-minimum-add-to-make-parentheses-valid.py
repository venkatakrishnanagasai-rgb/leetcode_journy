class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        moves = tally = 0

        for ch in s:
            if   ch =='(':
                tally+= 1
            elif ch ==')' and tally > 0:
                tally-= 1
            else:
                tally = 0
                moves+= 1
                
        return tally + moves