class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        le = len(s1)   

        for i in range(len(s2)):
            if s2[i] in count: 
                count[s2[i]] -= 1
            if i >= le and s2[i-le] in count: 
                count[s2[i-le]] += 1

            if all([count[i] == 0 for i in count]):
                return True

        return False