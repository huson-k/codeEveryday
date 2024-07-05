# 283. 移动零
    # 描述： 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    # 例子:
        # 输入: nums = [0,1,0,3,12]
        # 输出: [1,3,12,0,0]

from typing import List
import unittest

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        移动所有的 0 到数组的末尾，同时保持非零元素的相对顺序。
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
        return nums

class TestMoveZeroes(unittest.TestCase):
    def test_move_zeroes(self):
        solution = Solution()
        
        # 测试案例 1
        nums = [0, 1, 0, 3, 12]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])
        
        # 测试案例 2
        nums = [0, 0, 1]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 0, 0])
        
        # 测试案例 3
        nums = [1, 0, 1]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 1, 0])
        
        # 测试案例 4
        nums = [0, 1, 0, 3, 0, 0, 12, 0, 1]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 1, 0, 0, 0, 0, 0])
        
        # 测试案例 5
        nums = [0]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [0])
        
        # 测试案例 6
        nums = [1, 2, 3, 4, 5]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
