# given an array return true if there is a group of 3 intergers i,j,k such that i > j > lk and a[i] > a[j] >a[k]

def findthrees(array):
    first = 2 * 31
    f = -1
    second =  2 * 31 
    s = -1
    third = 0
    for i, n in enumerate(array):
        if n < first:
            first = n
            f = i
        elif n < second:
            second = n
            s = i
        else:
            print('FOUND, i = ', f, 'j = ', s, 'k=' , i  )
            return True
    
    return first != second != third != 0
    

print(findthrees([5,4,2,1,2,3]))
