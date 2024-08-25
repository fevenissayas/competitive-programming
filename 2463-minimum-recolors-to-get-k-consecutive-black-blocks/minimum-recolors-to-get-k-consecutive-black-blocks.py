class Solution:
    def minimumRecolors(self, blocksocks: str, k: int) -> int:
        op = sum(1 for i in range(k) if blocksocks[i] == 'W') 
        num = op
        for i in range(k, len(blocksocks)):
            if blocksocks[i - k] == 'W':
                num -= 1
            if blocksocks[i] == 'W':
                num += 1
            op = min(op, num)
        
        return op