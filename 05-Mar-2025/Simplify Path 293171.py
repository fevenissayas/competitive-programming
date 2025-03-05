# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        res = []
        for i in range(len(path)):
            if not path[i] or path[i] == '.':
                continue
            else:
                if res and path[i] == '..':
                    res.pop()
                elif path[i] != '..':
                    res.append(path[i])
        
        return '/' + '/'.join(res)