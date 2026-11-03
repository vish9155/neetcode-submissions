# class Solution:
#     def productExceptSelf(self, nums):
#         n = len(nums)
#         ans = []

#         for i in range(n):
#             product = 1

#             for j in range(n):
#                 if i != j:
#                     product *= nums[j]

#             ans.append(product)

#         return ans


   

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans

solution = Solution()
print(solution.productExceptSelf([1, 2, 4, 6]))  


        