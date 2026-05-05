class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1 
        result = []
        length = len(arr)

        for i in range(length-1,-1,-1): #reversed Itteration 
            if i==length-1:
                result.append(-1)
            else:
                result.append(greatest)
            greatest = max(greatest,arr[i])
        return result[::-1] #reversed


        