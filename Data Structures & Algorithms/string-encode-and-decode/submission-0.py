class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = []
        for word in strs:
            result.append(str(len(word)) + '#'+ word)
        encoded_string = ''.join(result)
        return encoded_string

        


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            word = s[start:end]
            result.append(word)
            i = end
        return result
