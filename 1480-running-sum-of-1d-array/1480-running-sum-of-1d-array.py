class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = 0
        ans = []

        for num in nums:
            run_sum = run_sum + num

            ans.append(run_sum)
        return ans