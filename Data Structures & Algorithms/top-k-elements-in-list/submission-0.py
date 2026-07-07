class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}

        for i, num in enumerate(nums):

            if num in  groups:
                groups[num]=groups[num]+1
            else:
                groups[num] = 1
            

        sorted_nums = sorted(groups, key=groups.get, reverse=True)
        return sorted_nums[:k]
