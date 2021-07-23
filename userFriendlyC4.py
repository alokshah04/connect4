import copy
import time
import random
from tqdm import tqdm

#for debugging
def getRows(b, r):
    return b[r]

def boardEvalSimple(b):
    score = 0
    for c in range(0, 7):
        r = 5
        columnPoints = 0
        if(c == 0 or c == 6):
            columnPoints = 1
        elif(c == 1 or c == 5):
            columnPoints = 4
        elif(c == 2 or c == 4):
            columnPoints = 7
        elif(c == 3):
            columnPoints = 10
        while r >= 0 and b[r][c] != " ":
            if b[r][c] == "X":
                score += columnPoints
            else:
                score -= columnPoints
            r -= 1
    return score

def boardEvalLessSimple(b):
  board_scores = [[3,4,5,7,5,4,3],[4,6,8,10,8,6,4],[5,8,11,13,11,8,5],[5,8,11,13,11,8,5],[4,6,8,10,8,6,4], [3,4,5,7,5,4,3]]
  score = 0
  for c in range(0,7):
    r = 5
    while r >= 0 and b[r][c] != " ":
      if b[r][c] == "X":
        score += board_scores[r][c]
      else:
        score -= board_scores[r][c]
      r -= 1
  return score

def navTree(b, depth, evalAlgo):
    if depth == 0:
        return (boardEvalLessSimple(b) if evalAlgo == 1 else boardEvalSimple(b))
    else:
        bv = -998
        moves = getlegalMoves(b)
        random.shuffle(moves)
        for c in moves:
            #make a deep copy of the board with flipped perspective
            b2 = [[('O' if (y == 'X') else ('X' if y == 'O' else ' ')) for y in x] for x in [r[:] for r in b]]
            #make another move
            r, c = move(b2, c, 'X'), c
            #test for a win before calling the function again
            if(verticalWinTest(b2, r, c) or 
                horizontalWinTest(b2, r, c, 'X') or
                diagonalWinTest(b2, r, c, 'X')):
                return -1000
            #search the tree
            val = navTree(b2, depth-1, evalAlgo)
            #update the best value
            bv = val if val > bv else bv
        return -1 * bv

#for debugging
def getColumns(b, c):
    return [r[c] for r in b]

#for debugging
def isLegalMove(b, r, c):
    return ((c-1 < 7) and (b[r][c-1] == '0'))

#temp
def getlegalMoves(board):
    playableColumns = []
    for col in range(0,7):
        if board[0][col] == " ":
            playableColumns.append(col)
    return playableColumns
    
def move(b, c, symbol):
    for r in reversed(range(6)):
            if ((c < 7) and (b[r][c] == ' ')):
                    b[r][c] = symbol
                    return int(r)

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
    '''
    human
    random
    smart
    smarter
    '''
    print("Hello, welcome to our Connect Four AI Project")
    print("We currently have four different player modes:\n")
    print("1) Manual - a user enters each move")
    print("2) Random - a bot makes random moves across the board")
    print("3) Smart - a bot uses a minimax algorithm generated with a column-only board evaluation routine")
    print("4) Smarter - a bot uses a minimax algorithm generated with a discrete based board evaluation that\n             evaluates the ways to win at each board location")
    player1 = input("Enter the mode for Player 1 (Xs) as it appears in the above description *CASE SENSITIVE:\n").lower()
    treeDepth1 = 0
    if "smart" in player1:
        treeDepth1 = int(input(f"Enter the tree depth for the {player1} algorithm:\n"))
    player2 = input("Enter the mode for Player 2 (Os) as it appears in the above description *CASE SENSITIVE:\n").lower()
    treeDepth2 = 0
    if "smart" in player2:
        treeDepth2 = int(input(f"Enter the tree depth for the {player2} algorithm:\n"))
    games = int(input("Enter the number of games you want to play:\n"))
    print()
    playerDict = {'X': player1, 'O': player2}
    winDict = {"X": 0, "O": 0}
    for i in tqdm(range(games)):
        board = [([' ' for i in range(7)]) for j in range(6)]
        symbol = 'X'
        moveCounter = 0
        while True:
            if(playerDict[symbol] == "random"):
                c = random.choice(getlegalMoves(board))
                r = move(board, c, symbol)
            elif(playerDict[symbol] == "smart" or playerDict[symbol] == "smarter"):
                moves = getlegalMoves(board)
                random.shuffle(moves)
                bestScore = -100000
                bestMove = 0
                for m in moves:
                    b2 = copy.deepcopy(board)
                    if(symbol == 'O'):
                        b2 = [[('O' if (y == 'X') else ('X' if y == 'O' else ' ')) for y in x] for x in [r[:] for r in b2]]
                    move(b2, m, 'X')
                    score = navTree(b2, (treeDepth1 if playerDict[symbol] == player1 else treeDepth2), 
                                    (0 if playerDict[symbol] == "smart" else 1))
                    if score > bestScore:
                        bestScore = score
                        bestMove = m
                r, c = move(board, bestMove, symbol), bestMove
            else:
                printBoard(board)
                m = input("Enter a Column(1-7) or F to quit: ")
                if (m == 'F'): 
                    break
                r, c = move(board, int(m)-1, symbol), int(m)-1

            if(verticalWinTest(board, r, c) or horizontalWinTest(board, r, c, symbol) or diagonalWinTest(board, r, c, symbol)):
                winDict[symbol] += 1
                if playerDict['X'] == 'human' or playerDict['O'] == 'human':
                    print(f"{symbol} wins!")
                break
            moveCounter+=1
            if(moveCounter == 42):
                if playerDict['X'] == 'human' or playerDict['O'] == 'human':
                    print("It's a tie!")
                break
            symbol = 'X' if symbol == 'O' else 'O'
    print("\nWins: ", winDict['X'])
    print("Losses: ", winDict['O'])
    print("Ties: ", games - winDict['X'] - winDict['O'])











