class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1

        while i<j:
            curr = nums[i]+nums[j]
            if curr < target :
                i=i+1
            elif curr  > target :
                j=j-1
            else:
                return[i,j]
        return []