from generic.generic import decode_list_to_str


def game_not_finished(grid):
    grid = decode_list_to_str(grid)
    # when neither side has three in a row but the grid still has empty cells
    if ' ' in grid and not x_wins(grid) and not o_wins(grid):
        print('Game not finished')


def draw(grid):
    grid = decode_list_to_str(grid)
    if ' ' not in grid:
        return True


def x_wins(grid):
    # when the grid has three X's in a row (including diagonals).
    grid = decode_list_to_str(grid)
    if horizontal_check(grid, 'X'):
        return True
    if vertical_check(grid, 'X'):
        return True
    if right_diagonal_check(grid, 'X'):
        return True
    if left_diagonal_check(grid, 'X'):
        return True
    return False


def o_wins(grid):
    # when the grid has three O's in a row (including diagonals).
    grid = decode_list_to_str(grid)
    if horizontal_check(grid, 'O'):
        return True
    if vertical_check(grid, 'O'):
        return True
    if right_diagonal_check(grid, 'O'):
        return True
    if left_diagonal_check(grid, 'O'):
        return True
    return False


def horizontal_check(grid, symbol):
    for i in range(0, 7, 3):
        if symbol == grid[i] and symbol == grid[i + 1] and symbol == grid[i + 2]:
            return True


def vertical_check(grid, symbol):
    for i in range(0, 3):
        if symbol == grid[i] and symbol == grid[i + 3] and symbol == grid[i + 6]:
            return True


def left_diagonal_check(grid, symbol):
    if symbol == grid[0] and symbol == grid[4] and symbol == grid[8]:
        return True


def right_diagonal_check(grid, symbol):
    if symbol == grid[2] and symbol == grid[4] and symbol == grid[6]:
        return True


def impossible(grid):
    grid = decode_list_to_str(grid)
    if x_wins(grid) and o_wins(grid):
        return True
    if 'XXX' in grid and 'OOO' in grid:
        return True
    if grid.count('O') != grid.count('X') and abs(grid.count('O') - grid.count('X')) >= 2:
        return True
