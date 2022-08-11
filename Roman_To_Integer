class Solution:
    
    def romanToInt(self, s: str) -> int:
        
        values={"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}
        
        total=0
        
        while len(s) >0:
            if len(s) > 1 and values[s[0]]<values[s[1]]:
                total += values[s[1]]-values[s[0]]
                s=s[2:]
            else:
                total += values[s[0]]
                s=s[1:]
        return total
