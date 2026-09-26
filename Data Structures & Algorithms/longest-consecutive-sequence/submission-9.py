class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, 1 
        length = 1
        max_length = 1
        res= set()

        if not nums:
            return 0
     
        while right < len(nums):
            if nums[right] == nums[left]:
                right+=1
                continue
            if nums[right] == nums[left]+1:
                res.add(nums[left])
                res.add(nums[right])
                length = len(res)

            else:
                res = set()
                length = 1
            
            max_length = max(max_length , length)
            left = right
            right+=1

        return max_length
            
                

