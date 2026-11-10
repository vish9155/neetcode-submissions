class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()

        for k in range(len(nums)-1):
            if k>0 and nums[k]==nums[k-1]:
                continue
            i,j=k+1,len(nums)-1
            while j>i:
                if nums[i]+nums[j]<-nums[k]:
                    i+=1
                elif nums[i]+nums[j]>-nums[k]:
                    j-=1
                else:
                    l.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[i] == nums[i-1]:
                        i+=1
                    while i<j and nums[j] == nums[j+1]:
                        j-=1
        return l                            
