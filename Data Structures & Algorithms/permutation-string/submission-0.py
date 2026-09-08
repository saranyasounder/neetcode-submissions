class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def get_frequency_string(window):
            freq_list = [0] * 26
            for char in window:
                freq_list[ord(char) - ord('a')] += 1
            return "".join(str(count) for count in freq_list)

        s1_fingerprint = get_frequency_string(s1)

        left = 0
        while left + len(s1) <= len(s2):
            window = s2[left : left + len(s1)]
            # your next step: compare get_frequency_string(window) to s1_fingerprint
            freq_string = get_frequency_string(window)
            if freq_string == s1_fingerprint:
                return True
            left += 1

        return False