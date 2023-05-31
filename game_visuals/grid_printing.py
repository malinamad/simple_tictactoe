from generic.generic import decode_list_to_str


def bottom_top_of_game():
    print('-' * 9)


def print_grid(grid):
    grid = decode_list_to_str(grid)
    bottom_top_of_game()
    for i in range(0, 7, 3):
        print(f"| {grid[i]} {grid[i + 1]} {grid[i + 2]} |")
    bottom_top_of_game()