class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        dict = {}
        maxlength=0
        for j in range(len(s)):
            if s[j] not in dict or dict[s[j]]<i:
                dict[s[j]] = j
                maxlength = max(maxlength,j - i + 1)

            else:
                i = dict[s[j]] + 1
                dict[s[j]] = j

        return maxlength
