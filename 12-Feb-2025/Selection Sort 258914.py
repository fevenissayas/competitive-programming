# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            temp = i
            for j in range(i+1, len(arr)):
                if arr[temp] > arr[j]:
                    temp = j
            arr[i], arr[temp] = arr[temp], arr[i]
        
        return arr