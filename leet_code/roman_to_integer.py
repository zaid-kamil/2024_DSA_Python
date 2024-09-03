class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I":1, "V":5, "X":10, "L":50,
            "C": 100, "D":500, "M": 1000,
            "IV":4, "IX":9, "XL":40, "XC":90,
            "CD": 400, "CM":900
        }

        total = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in values:
                total += values[s[i:i+2]]
                i += 2
            else:
                total += values[s[i]]
                i+=1
        return total
    
if __name__ == "__main__":
    s = "MCMXCIV"
    print(Solution().romanToInt(s))  # Output: 1994