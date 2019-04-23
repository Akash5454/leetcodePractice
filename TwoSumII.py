class Solution:
    def twoSum(self, numbers, target): 
        index=[]
        i = 0
        j = len(numbers)-1
        while(i<j):
            if numbers[i] + numbers[j] == target:
                index.extend([i+1,j+1])
                return(sorted(index))
            elif(numbers[i] + numbers[j] > target):
                j = j-1
            else:
                i = i+1