# p014 Longest Common Prefix
# Easy

# Write a function to find the longest common prefix string amongst an array of strings.

# """
# :type strs: List[str]
# :rtype: str
# """

class Solution(object):
    def longestCommonPrefix(self, strs):  # beats 53.82%

        result = ''
        if len(strs) == 0:
            return result

        for i in range(len(min(strs, key=len))):
            temp = []
            for j in range(len(strs)):
                temp.append(strs[j][i])
            if len(set(temp)) == 1:
                result += temp[0]
            else:
                break
        return result

    def longestCommonPrefix2(self, strs):  # beats 8.17%
        result = ''
        if len(strs) == 0:
            return result
        from collections import deque  # 利用deque的maxlen特性
        for i in range(len(min(strs, key=len))):
            temp = list(map(lambda x: deque(x[i], 1), strs))
            if temp.count(temp[0]) == len(temp):
                result += temp[0][0]
            else:
                break
        return result

if __name__ == '__main__':
    lst = ['Denis Xie', 'Dennis X', 'Dendi Den', 'Denn']
    lst2 = []
    assert Solution().longestCommonPrefix(lst)  == 'Den', 'regular test'
    assert Solution().longestCommonPrefix(lst2) == '', 'empty list'
    print('all passed')
