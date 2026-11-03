class Solution:
    def topKFrequent(self, nums, k) :
        d={}
        for x in nums:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        topk=sorted(d,key=d.get,reverse=True)[:k]   
        return topk

solution=Solution()
print(solution.topKFrequent([1,1,1,2,2,3,3,4,1,1],2))                 
        