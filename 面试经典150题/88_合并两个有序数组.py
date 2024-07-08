from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()

import unittest

class TestMerge(unittest.TestCase):
    def test_merge(self):
        solution = Solution()
        
        # 测试案例 1
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])
        
        # 测试案例 2
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])
        
        # 测试案例 3
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])
        
        # 测试案例 4
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])
        
        # 测试案例 5
        nums1 = [2, 0]
        m = 1
        nums2 = [1]
        n = 1
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2])

if __name__ == '__main__':
    unittest.main()
