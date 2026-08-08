class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        while i < n:
            corr_idx = nums[i] - 1

            if nums[i] != nums[corr_idx]:
                nums[i], nums[corr_idx] = nums[corr_idx], nums[i]

            else:
                i += 1
            
        for i in range(n):
            if nums[i] != i + 1:
                return  [nums[i], i + 1]
        