'''
Top K elements in the array
'''

# O(nLog(n)) Solution:
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = {}
        ends = []
        for i in range(len(nums)):
            # O(n)
            if nums[i] in dicts:
                dicts[nums[i]] += 1
            else:
                dicts[nums[i]] = 1
        ends = [(-value, key) for key,value in c.items()]
        heapq.heapify(ends)
        output = []
        for i in range(k):
            item = heapq.heappop(ends)
            output.append(item[1])
        return c[:k]
# Runtime: 119 ms
# Memory: 19.4 MB
# Runtime: 126 ms
# Memory: 19.7 MB

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = {}
        ends = []
        for i in range(len(nums)):
            # O(n)
            if nums[i] in dicts:
                dicts[nums[i]] += 1
            else:
                dicts[nums[i]] = 1
        # log(n) solution here
        for key, val in dicts.items():
            if len(ans) < k:
                freq[val].append(key)

        result = []
        for g in range(len(freq) -1, 0, -1):
            for n in freq[g]:
                result.append(n)
                if len(result) == k:
                    return result
