class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:  # only start counting from sequence beginnings
                current = num
                current_length = 1
                while current + 1 in num_set:
                    current += 1
                    current_length += 1
                max_length = max(max_length, current_length)

        return max_length