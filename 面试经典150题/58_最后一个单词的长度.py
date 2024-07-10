# 58. 最后一个单词的长度
    # 描述： 给定一个整数数组 nums 和一个整数目标值 target，
    # 请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
    # 例子:
        # 输入: nums = [2, 7, 11, 15], target = 9
        # 输出: [0, 1]

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 将字符串按空格分割成单词列表
        l = s.split()
        # 返回最后一个单词的长度
        return len(l[-1]) if l else 0

# 创建 Solution 类的实例
solution = Solution()

# 多个测试案例
test_cases = [
    " 这是 一个 示例 字符串， 包含 一些   空格！",
    "Hello World",
    "Python is great",
    " trailing space ",
    "singleword",
    " ",
    ""
]

# 执行测试案例并打印结果
for i, test in enumerate(test_cases):
    result = solution.lengthOfLastWord(test)
    print(f"Test case {i+1}: '{test}' -> Length of last word: {result}")
