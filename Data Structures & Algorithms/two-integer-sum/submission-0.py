class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs={}
        result=[]
        for i in range(len(nums)):
            diff=target-nums[i]
            if nums[i] in pairs:
                result.append(pairs.get(nums[i]))
                result.append(i)
                return sorted(result)
            else:
                pairs[diff]=i
        return result
        