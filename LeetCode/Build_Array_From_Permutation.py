class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in range(len(nums)):
            ans.append(x)

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans