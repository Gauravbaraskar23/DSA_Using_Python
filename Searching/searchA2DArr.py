# 74. Search a 2D Matrix

def searchMatrix(matrix , target):
    rows = len(matrix)
    cols = len(matrix[0])
    
    l = 0
    r = rows * cols -1
    
    while l <= r:
        mid = (l+r)//2
        
        i =mid//cols
        j = mid %cols
        if matrix[i][j] == target:
            return True 
        
        elif matrix[i][j] > target:
            r= mid -1
        
        else:
            l = mid +1
            
    return False
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]] , 34))