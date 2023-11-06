''' Puzzle '''
def validate_board(board):
    '''
    >>> validate_board(board)
    False
    '''
    for i in range(9):
        row_counts = {}
        col_counts = {}
        for j in range(9):
            row_digit = board[i][j]
            column_digit = board[j][i]

            if row_digit != ' ':
                if row_digit in row_counts:
                    return False
                row_counts[row_digit] = 1

            if column_digit != ' ':
                if column_digit in col_counts:
                    return False
                col_counts[column_digit] = 1

    for color in range(1, 10):
        result = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == str(color):
                    result.append((i, j))

        if len(result) != 9:
            return False

        for i in range(9):
            for j in range(9):
                if (i, j) not in result:
                    if board[i][j] != ' ':
                        return False

    return True

board = [
"**** ****",
"***1 ****",
"**  3****",
"* 4 1****",
"     9 5 ",
" 6  83  *",
"3   1  **",
"  8  2***",
"  2  ****"
]

result = validate_board(board)
print(result)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())