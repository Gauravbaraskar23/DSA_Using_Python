#54. Spiral Matrix: Given mxn matrix, return all elements of the matrix in spiral order.

matrix = [[1,2,3] , [4,5,6],[7,8,9], [10,11,12]] 

n = len(matrix)
m = len(matrix[0])
total = n*m

ans = []
count = 0

rowstart = 0
colstart = 0

rowend = n - 1
colend = m -1


while count < total:
    # rowstart , colstart -> colend
    for i in range(colstart, colend+1) :
        ans.append(matrix[rowstart][i])
        count += 1
    rowstart += 1
        
    if count == total:
        break
    # colend , rowstart -> rowend
    for i in range(rowstart,rowend+1):
        ans.append(matrix[i][colend])
        count +=1
    colend -= 1
    
    if count == total:
        break
    
    # rowend , colend -> colstart
    for i in range(colend ,colstart-1,-1):
        ans.append(matrix[rowend][i])
        count +=1
    rowend -=1
    
    if count == total:
        break   
    
    # colstart , rowend ->rowstart
    for i in range(rowend, rowstart-1,-1):
        ans.append(matrix[i][colstart])
        count +=1
    colstart += 1 
    

print(ans)
    
    
