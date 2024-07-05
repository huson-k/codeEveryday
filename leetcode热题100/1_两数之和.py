# 1. 两数之和
    # 描述： 给定一个整数数组 nums 和一个整数目标值 target，
    # 请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
    # 例子:
        # 输入: nums = [2, 7, 11, 15], target = 9
        # 输出: [0, 1]

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

def test_twoSum():
    solution = Solution()

    # Test case 1: Standard case
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1], "Test case 1 failed"

    # Test case 2: No solution
    assert solution.twoSum([1, 2, 3], 7) == None, "Test case 2 failed"

    # Test case 3: Multiple pairs, only one solution
    assert solution.twoSum([3, 2, 4, 3], 6) == [0, 3], "Test case 3 failed"

    # Test case 4: List with negative numbers
    assert solution.twoSum([-1, -2, 3, 4], 2) == [0, 2], "Test case 4 failed"

    # Test case 5: Large numbers
    assert solution.twoSum([1000, 2000, 3000, 5000], 8000) == [2, 3], "Test case 5 failed"

    # Test case 6: Target is zero
    assert solution.twoSum([-3, 4, 3, 90], 0) == [0, 2], "Test case 6 failed"

    # Test case 7: Numbers repeating, where only one should be used
    assert solution.twoSum([1, 3, 3, 4], 6) == [1, 2], "Test case 7 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_twoSum()
