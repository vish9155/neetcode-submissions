class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
        return [] 

solution=Solution()
print(solution.twoSum([3,4,5,6],10))                   
        