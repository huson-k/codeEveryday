# 136. 只出现一次的数字
    # 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    # 例子:
        # 输入：nums = [2,2,1]
        # 输出：1

from typing import List
import unittest

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i

class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        solution = Solution()
        
        # 测试案例 1
        nums = [2, 2, 1]
        result = solution.singleNumber(nums)
        self.assertEqual(result, 1)
        
        # 测试案例 2
        nums = [4, 1, 2, 1, 2]
        result = solution.singleNumber(nums)
        self.assertEqual(result, 4)
        
        # 测试案例 3
        nums = [1]
        result = solution.singleNumber(nums)
        self.assertEqual(result, 1)
        
        # 测试案例 4
        nums = [0, 0, 1, 1, 99]
        result = solution.singleNumber(nums)
        self.assertEqual(result, 99)
        
        # 测试案例 5
        nums = [17, 12, 5, 12, 5]
        result = solution.singleNumber(nums)
        self.assertEqual(result, 17)
        
        # 测试案例 6
        nums = [-1, -1, -2]
        result = solution.singleNumber(nums)
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()
