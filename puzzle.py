''' Puzzle '''
def validate_board(board: list)-> bool:
    '''
    Function to set whether the logic puzzle board is ready to start playing
    >>> validate_board(["**** ****//n", "***1 ****//n", "**  3****//n", "* 4 1****//n",\
"     9 5 //n", " 6  83  *//n", "3   1  **//n", "  8  2***//n", "  2  ****//n"])
    False
    '''
    for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                digits = set()
                for k in range(3):
                    for l in range(3):
                        cell = board[i + k][j + l]
                        if cell == ' ':
                            continue
                        if cell in digits:
                            return False
                        digits.add(cell)
    for i in range(9):
        row_digits = set()
        col_digits = set()
        for j in range(9):
            row_square = board[i][j]
            col_squere = board[j][i]

            if row_square == ' ' or col_squere == ' ':
                continue

            if row_square in row_digits or col_squere in col_digits:
                return False

            row_digits.add(row_square)
            col_digits.add(col_squere)
    return True

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
