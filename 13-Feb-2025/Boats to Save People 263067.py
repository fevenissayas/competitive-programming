# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        i = 0
        j = len(people)-1

        while i <= j:        
            if people[j] + people[i] <= limit:
                i += 1
                
            j -= 1
            count += 1
                
        return count