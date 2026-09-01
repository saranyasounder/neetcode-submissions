class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        hashmap = {}

        def get_frequency_string(word):
            freq_list = [0] * 26
            for char in word:
                freq_list[ord(char) - ord('a')] += 1
            freq_string = []
            char = 'a'
            for position in freq_list:
                freq_string.append(char)
                freq_string.append(str(position))
                char = chr(ord(char) + 1)
            return ''.join(freq_string)
        
        for word in strs:
            freq_string = get_frequency_string(word)
            if freq_string not in hashmap:
                hashmap[freq_string] = []
            hashmap[freq_string].append(word)
        
        return list(hashmap.values())


        