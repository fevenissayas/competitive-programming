class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        for operation in operations:
            if operation == '+':
                lst.append(lst[-1] + lst[-2])
            elif operation == 'D':
                lst.append(lst[-1]*2)
            elif operation == 'C':
                lst.pop(-1)
            else:
                lst.append(int(operation))
                
        return sum(lst)