"""
Tung Hoang - 12/03/19

The program was modified from a starter code. The program checks whether
the table that the user entered is a magic square.

https://www.wikihow.com/Solve-a-Magic-Square#:~:targetText=To%20solve%20an%20odd
%2Dnumbered,the%20magic%20constant%20is%2015.

"""

def fillSquare(n, sqArr):
    '''
    This procedure prompts the user for n^2 inputs to populate a
    2D square array which has alreay been declared
    precondition:  sqArr has been declared with a size of nxn
    '''
    for r in range(n):
        print("----ROW " + str(r + 1) + "----")
        for c in range(n):
            sqArr[r][c] = int(input("Enter value: "))
    

def printSquare(n, sqArr):
    '''
    This procedure "pretty" prints a 2D square array of size n
    '''
    for r in range(n):
        for c in range(n):
            print(sqArr[r][c], end="\t")
        print("\n")
    
def checkRow(n, sqArr, mNum):
    '''
    This procedure will return true if every row of sqArr has a
    sum of mNum
    '''
    sumRow = 0
    for row in range(n):
        for col in range(n):
            sumRow += sqArr[row][col]
            
        if sumRow != mNum:
            return False
        sumRow = 0
        
    return True

def checkCol(n, sqArr, mNum):
    '''
    This procedure will return true if every column of sqArr has a
    sum of mNum
    '''
    sumCol = 0
    for col in range(n):
        for row in range(n):
            sumCol += sqArr[row][col]
            
        if sumCol != mNum:
            return False
        sumCol = 0
        
    return True

def checkDiag1(n, sqArr, mNum):
    '''
    This procedure will return true if the row from top left to
    bottom right of sqArr has a sum of mNum
    '''
    sumDiag1 = 0
    for index in range(n):
        sumDiag1 += sqArr[index][index]
            
    if sumDiag1 != mNum:
        return False
        
    return True

def checkDiag2(n, sqArr, mNum):
    '''
    This procedure will return true if the row from top right to
    bottom left of sqArr has a sum of mNum
    '''
    sumDiag2 = 0
    col = n - 1
    for row in range(n):
        sumDiag2 += sqArr[row][col]
        col -= 1
            
    if sumDiag2 != mNum:
        return False
        
    return True

def checkUnique(n, sqArr):
    '''
    This procedure checks if whether every number in the table is
    unique from one another.
    '''
    numlist = []
    for row in range(n):
        for col in range(n):
            currNum = sqArr[row][col]

            if currNum in numlist:
                return False
            numlist.append(currNum)
            
    return True

def checkSquare(size, square):
    '''
    Returns True if inputed square is magic, and False if not.
    '''
    magicNum = size * (size**2 + 1) / 2
    if(checkRow(size, square, magicNum) and  \
       checkCol(size, square, magicNum) and  \
       checkDiag1(size, square, magicNum) and  \
       checkDiag2(size, square, magicNum) and   \
       checkUnique(size, square)):
       return "This is a magic square"
    else:
       return "This is not a magic square"



# ---MAIN---

# Prompt user for the table
s = int(input("Enter square side length:  "))
sq = [[0 for x in range(s)] for y in range(s)]
fillSquare(s, sq)

# Print out the table and determine whether it is a magic square
printSquare(s, sq)
print(checkSquare(s, sq))
   

