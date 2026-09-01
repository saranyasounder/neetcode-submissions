class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for key, frequency in hashmap.items():
            bucket[frequency].append(key)
        result = []
        for i in reversed(range(len(nums)+1)):
            for value in bucket[i]:
                if len(result) < k:
                    result.append(value)
                else:
                    return result
        return result

