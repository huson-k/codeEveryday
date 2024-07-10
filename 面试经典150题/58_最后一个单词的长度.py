# 58. 最后一个单词的长度
    # 描述： 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
    # 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串
    # 例子:
        # 输入：s = "Hello World"
        # 输出：5

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
