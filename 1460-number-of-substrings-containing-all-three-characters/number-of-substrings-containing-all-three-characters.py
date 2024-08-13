class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        temp = j = 0
        val = {"a": 0, "b": 0, "c": 0}
        
        for i in range(n):
            val[s[i]] += 1            
            while val["a"]  >  0 and val["b"]  >  0 and val["c"]  >  0:
                temp += n - i
                val[s[j]] -= 1
                j += 1
        
        return temp