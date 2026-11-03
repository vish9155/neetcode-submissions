class Solution:

    def encode(self, strs):
        ans=""
        for s in strs:
            ans+=str(len(s))+"$"+s
        return ans    

    def decode(self, s):
        ans=[]
        i=0

        while i<len(s):
            j=i
            while s[j]!="$":
                j+=1
            l=int(s[i:j]) 
            ans.append(s[j+1:j+1+l])
            i=j+1+l
        return ans

solution=Solution()

encoded = solution.encode(["vishal", "kumar"])
print("Encoded:", encoded)

decoded = solution.decode(encoded)
print("Decoded:", decoded)


