# 28 找出字符串中第一个匹配项的下标
    # 描述： 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
    # 如果 needle 不是 haystack 的一部分，则返回  -1 。
    # 例子:
        # 输入：haystack = "sadbutsad", needle = "sad"
        # 输出：0

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1

# 测试案例
def test_strStr():
    solution = Solution()
    
    # 正常情况
    assert solution.strStr("hello", "ll") == 2
    assert solution.strStr("aaaaa", "bba") == -1
    assert solution.strStr("mississippi", "issi") == 1
    assert solution.strStr("abcdef", "def") == 3
    
    # 边界情况
    assert solution.strStr("", "") == 0
    assert solution.strStr("a", "") == 0
    assert solution.strStr("", "a") == -1
