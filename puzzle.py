''' Puzzle '''
def validate_board(board: list)-> bool:
    '''
    Function to set whether the logic puzzle board is ready to start playing
    >>> validate_board(["**** ****//n", "***1 ****//n", "**  3****//n", "* 4 1****//n",\
"     9 5 //n", " 6  83  *//n", "3   1  **//n", "  8  2***//n", "  2  ****//n"])
    False
    >>> validate_board(["*  *  *  //n", "* 1* *  * //n", "* * 3* * *//n", " 4* 1* * *//n",\
"     9 5 //n", " 6  8*3  *//n", "3   1* * * //n", "  8  2*** //n", "  2  * * * //n"])
    True
    '''
    for i in range(9):
        digits = set()
        for j in range(9):
            cell = board[i][j]
            if cell in digits or (cell.isdigit() and int(cell) > 0 and int(cell) <= 9):
                digits.add(cell)
            elif cell != ' ' and cell != '*':
                return False

    # Validate columns
    for i in range(9):
        digits = set()
        for j in range(9):
            cell = board[j][i]
            if cell in digits or (cell.isdigit() and int(cell) > 0 and int(cell) <= 9):
                digits.add(cell)
            elif cell != ' ' and cell != '*':
                return False

    # Validate blocks
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            digits = set()
            for i in range(3):
                for j in range(3):
                    cell = board[block_row + i][block_col + j]
                    if cell in digits or (cell.isdigit() and int(cell) > 0 and int(cell) <= 9):
                        digits.add(cell)
                    elif cell != ' ' and cell != '*':
                        return False

    return True

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
