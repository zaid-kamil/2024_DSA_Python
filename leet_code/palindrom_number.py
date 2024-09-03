# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x =  str(x)
#         if x == x[::-1]:
#             return True
#         return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x !=0):
            return False
        rev = 0
        while x > rev:
            rev = rev*10 + x%10
            x //= 10
        return x == rev or x == rev // 10

if __name__ == "__main__":
    inp = 121
    print(Solution().isPalindrome(inp))  # Output: True
    inp = -121
    print(Solution().isPalindrome(inp))  # Output: False