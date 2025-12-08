from typing import List, Optional, Dict, Tuple, Set

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left, right = 0, n - 1
        pre_max, suf_max = 0, 0
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
        

if __name__ == '__main__':
    s = Solution()
    # 测试用例:
    testCase = [4,2,0,3,2,5]
    result = s.trap(testCase)
    print(result)
