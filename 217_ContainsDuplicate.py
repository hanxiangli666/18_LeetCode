from typing import List  # <--- 1. 解决 List 报错
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True