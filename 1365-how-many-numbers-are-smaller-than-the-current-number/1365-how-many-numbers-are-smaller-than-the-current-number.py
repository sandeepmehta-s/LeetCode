class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)

        first_occ = {}

        for i in range(len(sorted_num)):
            if sorted_num[i] not in first_occ:
                first_occ[sorted_num[i]] = i
        
        res = []

        for num in nums:
            res.append(first_occ[num])
        return res