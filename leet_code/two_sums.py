# Two sums is a dictionary question
# Time: O(n)
# Space: O(n)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}       
        for idx,value in enumerate(nums):
            x = target - value
            if x in map:
                return [idx, map[x]]
            map[value]=idx            

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))  # Output: [0, 1]