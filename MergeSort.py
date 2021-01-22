# MergeSort implementation 
#

def mergeSort(listToSort):
    
    if len(listToSort) > 1:
        #Find the midpoint of the array and divide into 2
        midpoint = int(len(listToSort) / 2) 
        left = listToSort[:midpoint]
        right = listToSort[midpoint:]


        print("left: ", left)
        print("right: ", right)

        mergeSort(left)
        # [16, 29] 
        mergeSort(right)
        # [8, 13, 17] => [8], [13, 17]
        
        leftCursor = 0
        rightCursor = 0
        resultCursor = 0

        while leftCursor < len(left) and rightCursor < len(right):
            if left[leftCursor] < right[rightCursor]:
                listToSort[resultCursor] = left[leftCursor]
                leftCursor += 1
            else: # right[rightCursor] <= left[leftCursor] 
                listToSort[resultCursor] = right[rightCursor] 
                rightCursor += 1
            resultCursor +=1 
        
        while (leftCursor < len(left)):
            listToSort[resultCursor] = left[leftCursor]
            leftCursor +=1
            resultCursor += 1
        while (rightCursor < len(right)):
            listToSort[resultCursor] = right[rightCursor]
            rightCursor +=1
            resultCursor += 1

        return listToSort   
   
def mergeRunner():
    #
    listToSort = [29, 16, 17, 13, 8]
    mergeSort(listToSort)
    print(listToSort)

# [16, 29] 
# [8, 13, 17] 

# [8, 13, 16, 17, 29]

if __name__ == '__main__': 
   mergeRunner()
 