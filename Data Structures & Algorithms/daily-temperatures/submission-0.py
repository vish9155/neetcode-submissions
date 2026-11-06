class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for x in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[x] >=temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans[x]=stack[-1]-x
            stack.append(x)
        return ans            
solution=Solution()
print(solution.dailyTemperatures([30,38,30,36,35,40,28]))