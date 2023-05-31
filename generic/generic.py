def update_the_grid(grid, coordinates, symbol):
    grid[coordinates[0]][coordinates[1]] = symbol


def convert_string_to_list(grid):
    """ Return grid as a list for players move """
    grid_lst = []
    for i in range(0, 7, 3):
        grid_lst.append([grid[i], grid[i + 1], grid[i + 2]])
    return grid_lst


def decode_list_to_str(grid):
    """ Return the string of a grid provided, and is to be used in already written code
    to avoice rewriting and modifying it. """
    grid_str = ''
    for symbols_row in grid:
        for symbol in symbols_row:
            grid_str += symbol
    return grid_str
