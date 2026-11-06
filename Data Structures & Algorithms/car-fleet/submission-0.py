class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[]

        for p,s in zip(position,speed):
            time=(target-p)/s
            pairs.append((p,time))
        
        pairs.sort(reverse=True)
        stack=[]
        for p,time in pairs:
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)

solution=Solution()
print(solution.carFleet( 12,
    [10, 8, 0, 5, 3],
    [2, 4, 1, 1, 3]))