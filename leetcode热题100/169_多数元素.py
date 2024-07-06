# 169. 多数元素
    # 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
    # 例子:
        # 输入：nums = [3,2,3]
        # 输出：3

from typing import List
import unittest

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        for i in unique_nums:
            if nums.count(i) > len(nums) / 2:
                return i

class TestMajorityElement(unittest.TestCase):
    def test_majority_element(self):
        solution = Solution()
        
        # 测试案例 1
        nums = [3, 2, 3]
        result = solution.majorityElement(nums)
        self.assertEqual(result, 3)
        
        # 测试案例 2
        nums = [2, 2, 1, 1, 1, 2, 2]
        result = solution.majorityElement(nums)
        self.assertEqual(result, 2)
        
        # 测试案例 3
        nums = [1]
        result = solution.majorityElement(nums)
        self.assertEqual(result, 1)
        
        # 测试案例 4
        nums = [1, 1, 2, 2, 2, 2]
        result = solution.majorityElement(nums)
        self.assertEqual(result, 2)
        
        # 测试案例 5
        nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
        result = solution.majorityElement(nums)
        self.assertEqual(result, 4)
        
        # 测试案例 6
        nums = [6, 5, 5]
        result = solution.majorityElement(nums)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

