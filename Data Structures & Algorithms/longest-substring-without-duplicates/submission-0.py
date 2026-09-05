class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left, right = 0, 0

        seen = {}

        while right < len(s):
            if s[right] not in seen or seen[s[right]] < left:
                seen[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
                right += 1
            else:
                left = seen[s[right]] + 1
                seen[s[right]] = right
                right += 1

        return maxLength