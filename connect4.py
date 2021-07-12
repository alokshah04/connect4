def getRows(b, r):
    return b[r]
    
def getColumns(b, c):
    return [r[c] for r in b]

def move(b, c, symbol):
    for r in reversed(range(6)):
        if isLegalMove(b, r, c):
            b[r][c-1] = symbol
            return (r, c)

def isLegalMove(b, r, c):
    return ((c-1 < 7) and (b[r][c-1] == '-'))

def printBoard(gameBoard): 
  print('  1   2   3   4   5   6   7 ')
  print('-----------------------------')
  currentRow=0
  for row in gameBoard:
    currentRow+=1
    print('|', end = '')
    for spot in row:
      print(' '+str(spot)+' |', end = '')
    if(currentRow<6):
      print('\n----+---+---+---+---+---+----')
    else:
      print('\n-----------------------------')
  
def winTest(b, lastMove):
  #check rows
  
  #check columns
  #check diagonals
  return 0


if __name__ == "__main__":
    board = [(['-' for i in range(7)]) for j in range(6)]
    printBoard(board)
    