def activeInactiveEvaluationRoutine(b):
    score = 0
    for c in range(0, 7):
        for r in range(0, 6):
            if b[r][c] != " ":
                if b[r][c] == "X":
                    symbol, opposing_symbol = "X", "O"
                else:
                    symbol, opposing_symbol = "O", "X"
                num_horiz, num_vert, num_diag_ne_sw, num_diag_nw_se = 0, 0, 0, 0

                scoreHoriz = 0
                rightBound = c + 3 if c + 3 <= 6 else 6
                leftBound = c - 3 if c - 3 >= 0 else 0
                column = c + 1
                while column <= rightBound and b[r][column] != opposing_symbol:
                    scoreHoriz += 1
                    column += 1
                column = c - 1
                while column >= leftBound and b[r][column] != opposing_symbol:
                    scoreHoriz += 1
                    column -= 1
                num_horiz = scoreHoriz - 2 if scoreHoriz >= 3 else 0

                scoreVert = 0
                lowerBound = r - 3 if r - 3 >= 0 else 0
                upperBound = r + 3 if r + 3 <= 5 else 5
                row = r - 1
                while row >= lowerBound and b[row][c] != opposing_symbol:
                    scoreVert += 1
                    row -= 1
                row = r + 1
                while row <= upperBound and b[row][c] != opposing_symbol:
                    scoreVert += 1
                    row += 1
                num_vert = scoreVert - 2 if scoreVert >= 3 else 0


                scoreNESW, scoreNWSE = 0, 0
                topBound = r - 3 if r - 3 >= 0 else 0
                bottomBound = r + 3 if r + 3 < 6 else 5
                leftBound = c - 3 if c - 3 >= 0 else 0
                rightBound = c + 3 if c + 3 < 7 else 6

                # NESW
                row = r - 1
                column = c + 1
                while row >= topBound and column <= rightBound and b[row][column] != opposing_symbol:
                    scoreNESW += 1
                    row -= 1
                    column += 1
                row = r + 1
                column = c - 1
                while row <= bottomBound and column >= leftBound and b[row][column] != opposing_symbol:
                    scoreNESW += 1
                    row += 1
                    column -= 1
                num_diag_ne_sw = scoreNESW - 2 if scoreNESW >= 3 else 0

                # NWSE
                row = r - 1
                column = c - 1
                while row >= topBound and column >= leftBound and b[row][column] != opposing_symbol:
                    scoreNWSE += 1
                    row -= 1
                    column -= 1
                row = r + 1
                column = c + 1
                while row <= bottomBound and column <= rightBound and b[row][column] != opposing_symbol:
                    scoreNWSE += 1
                    row += 1
                    column += 1
                num_diag_nw_se = scoreNWSE - 2 if scoreNWSE >= 3 else 0

                if (symbol == "X"):
                    score += num_horiz + num_vert + num_diag_ne_sw + num_diag_nw_se
                else:
                    score -= num_horiz + num_vert + num_diag_ne_sw + num_diag_nw_se
    return score