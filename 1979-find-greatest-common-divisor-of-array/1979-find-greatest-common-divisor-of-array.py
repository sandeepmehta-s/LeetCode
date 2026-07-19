class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s = min(nums)
        l = max(nums)

        while l % s != 0:
            temp = s

            s = l % s

            l =  temp
        return s