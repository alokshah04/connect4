import time
import random

#for debugging
def getRows(b, r):
		return b[r]

def boardEval(board):
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


def navTree(b, depth, move):
	if depth == 0:
		return boardEval(b)
	else:
		print('hello world')
		bv = -998
		for c in getlegalMoves(b):
			#make a deep copy of the board with flipped perspective
			b2 = [[('O' if y == 'X' else 'X') for y in x] for x in [r[:] for r in b]]
			#make another move
			r, c = move(b2, c, 'X'), c-1
			#test for a win before calling the function again
			if(verticalWinTest(b, r, c) or 
				horizontalWinTest(b, r, c, 'X') or 
				diagonalWinTest(b, r, c, 'O') or
				horizontalWinTest(b, r, c, 'O') or 
				diagonalWinTest(b, r, c, 'X')):
				return -1000
			#search the tree
			val = navTree(b2, depth-1, c)
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
		playerDict = {'X': "Computer", 'O': "Computer"}
		winDict = {'X': 0, 'O': 0}
		for i in range(10000):
			board = [([' ' for i in range(7)]) for j in range(6)]
			symbol = 'X'
			moveCounter = 0
			while True:
				if(playerDict[symbol] == "Computer"):
					c = random.choice(getlegalMoves(board))
					r = move(board, c, symbol)
				else:
					m = input("Enter a Column(1-7) or F to quit: ")
					if (m == 'F'): 
						break
					r, c = move(board, int(m)-1, symbol), int(m)-1

				printBoard(board)
				if(verticalWinTest(board, r, c) or horizontalWinTest(board, r, c, symbol) or diagonalWinTest(board, r, c, symbol)):
					winDict[symbol] += 1
					print(f"{symbol} wins!")
					break
				moveCounter+=1
				if(moveCounter == 42):
					print("It's a tie!")
					break
				symbol = 'X' if symbol == 'O' else 'O'


		print(winDict)

