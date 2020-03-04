class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        repeat = maxSub = 0

        for elem in s:
            if elem not in sub:
                sub += elem
                maxSub = max(len(sub), maxSub)
            else:
                sub.remove(sub[repeat])
                repeat += 1

        return maxSub
