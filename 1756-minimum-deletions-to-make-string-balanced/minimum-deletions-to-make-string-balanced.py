class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = delete = 0
        for i in s:
            if i == 'a':
                delete = min(delete + 1, b)
            else:
                b += 1   
        
        return delete