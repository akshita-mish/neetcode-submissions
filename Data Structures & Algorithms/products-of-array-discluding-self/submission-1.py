class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        cnt = 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
              
                cnt += 1

        result = []
        for num in nums:
            if cnt >= 2:
                result.append(0)
            elif cnt == 1:
                if num == 0:
                    result.append(prod)
                else:
                    result.append(0)
            else:
                result.append(prod // num)

        return result
        