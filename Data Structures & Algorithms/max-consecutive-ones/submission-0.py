class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        maxi=0
        for num in nums:
            if num!=0:
                cnt+=1
                if cnt>maxi:
                    maxi=cnt
            else:
                cnt=0
        return maxi