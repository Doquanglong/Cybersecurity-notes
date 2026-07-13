

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        print(freq)
       
nums = [1, 2, 2, 3, 3, 3,3]
sol = Solution()
sol.topKFrequent(nums, 2)