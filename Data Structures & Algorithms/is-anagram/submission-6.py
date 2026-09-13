class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
        count_t = {}
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

        for char, n in count_s.items():
            if char not in count_t:
                return False
            if n != count_t[char]:
                return False
        return True