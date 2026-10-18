class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:

                if num[i] + num[left] + num[right] == 0:
                    if [num[i], num[left], num[right]] not in result:
                        result.append([num[i], num[left], num[right]])
                    left += 1
                    right -= 1
                elif num[i] + num[left] + num[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result
        