class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        hm1 = {}
        hm2 = {}

        # Count characters of s1
        for ch in s1:
            hm1[ch] = hm1.get(ch, 0) + 1

        k = len(s1)
        l = 0

        for r in range(len(s2)):

            # Add character
            hm2[s2[r]] = hm2.get(s2[r], 0) + 1

            # Maintain window size
            if r - l + 1 > k:

                hm2[s2[l]] -= 1

                if hm2[s2[l]] == 0:
                    del hm2[s2[l]]

                l += 1

            # Compare frequency
            if hm1 == hm2:
                return True

        return False