class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        # process the first window
        min_score = nums[k-1] - nums[0]

        for right in range(k, len(nums)):
            left = right - k + 1

            res = nums[right]- nums[left]

            min_score = min(res, min_score)


        return min_score


