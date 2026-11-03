class Solution:
    def longestConsecutive(self, nums):
        longest=0
        s=set(nums)
        for x in s:
            if x-1 not in s:
                i=1
                while x+i in s:
                    i+=1
                longest=max(i,longest)
        return longest

solution=Solution()
print(solution.longestConsecutive([1,2,3,100,4,200]))