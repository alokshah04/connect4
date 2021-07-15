import time

#for debugging
def getRows(b, r):
    return b[r]

#for debugging
def getColumns(b, c):
    return [r[c] for r in b]

#for debugging
def isLegalMove(b, r, c):
    return ((c-1 < 7) and (b[r][c-1] == '-'))

def move(b, c, symbol):
    for r in reversed(range(6)):
        if ((c-1 < 7) and (b[r][c-1] == '-')):
            b[r][c-1] = symbol
            print()
            return r


def printBoard(gameBoard): 
  print("\n\n\n\n\n\n\n\n\n\n")
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

def verticalWinTest(b, r, c):
  return ((r <= 2) and (b[r][c] == b[r+1][c]) and (b[r][c] == b[r+2][c]) and (b[r][c] == b[r+3][c]))


def horizontalWinTest(b, lastR, lastC, lastSymbol):
  right = 0
  left = 0
  rightBound = 6
  leftBound = 0
  if lastC + 3 <= 6:
    rightBound = lastC + 3
  if lastC - 3 >= 0:
    leftBound = lastC - 3
  column = lastC + 1
  while column <= rightBound and b[lastR][column] == lastSymbol:
    right += 1
    column += 1
  column = lastC - 1
  while column >= leftBound and b[lastR][column] == lastSymbol:
    left += 1
    column -= 1
  return right + left >= 3

def diagonalWinTest(b, lastR, lastC, lastSymbol):
  # bottom left to top right test
  diagCount1 = 0
  topRightR = lastR
  topRightC = lastC
  while topRightR >= 0 and topRightC <= 6 and b[topRightR][topRightC] == lastSymbol:
    diagCount1 += 1
    topRightR -= 1
    topRightC += 1
  bottomLeftR = lastR + 1
  bottomLeftC = lastC - 1
  while bottomLeftR <= 5 and bottomLeftC >= 0 and b[bottomLeftR][bottomLeftC] == lastSymbol:
    diagCount1 += 1
    bottomLeftR += 1
    bottomLeftC -= 1
  if diagCount1 >= 4 :
    return True
  else: 
    # bottom right to top left test
    diagCount2 = 0
    topLeftR = lastR
    topLeftC = lastC
    while topLeftR >= 0 and topLeftC >= 0 and b[topLeftR][topLeftC] == lastSymbol:
      diagCount2 += 1
      topLeftR -= 1
      topLeftC -= 1
    bottomRightR = lastR + 1
    bottomRightC = lastC + 1
    while bottomRightR <= 5 and bottomRightC <= 6 and b[bottomRightR][bottomRightC] == lastSymbol:
      diagCount2 += 1
      bottomRightR += 1
      bottomRightC += 1
    return diagCount2 >= 4


if __name__ == "__main__":
    board = [(['-' for i in range(7)]) for j in range(6)]
    printBoard(board)
    symbol = 'X'
    while True:
      m = input("Enter a Column(1-7) or F to quit: ")
      if (m == 'F'): 
        break
      r, c = move(board, int(m), symbol), int(m)-1
      printBoard(board)
      if(verticalWinTest(board, r, c) or horizontalWinTest(board, r, c, symbol) or diagonalWinTest(board, r, c, symbol)):
        print(f"{symbol} wins!")
        break
      printBoard(board)
      symbol = 'X' if symbol == "O" else 'O'
    