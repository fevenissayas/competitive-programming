# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Counter()
        target = Counter(t)
        leng = float('inf')
        min_window = ""

        if s == t:
            return s
        
        left = end = start = 0

        def check(window, target):
            for elem in target:
                if elem not in window:
                    return False
                elif window[elem] < target[elem]:
                    return False
            return True                               
        
        for right in range(len(s)):
            if s[right] in target:
                window[s[right]] += 1
            
            while check(window, target):
                if leng > right-left+1:
                    start = left
                    end = right + 1
                leng = min(leng, right-left+1)
    
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del (window[s[left]])

                left += 1

        return s[start:end]