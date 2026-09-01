class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = [0] * 26
        
        for char in s:
            hashmap[ord(char) - ord('a')] += 1
        for char in t:
            hashmap[ord(char) - ord('a')] -= 1
        
        for count in hashmap:
            if count != 0:
                return False
        return True