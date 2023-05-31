from game_visuals.grid_printing import print_grid
from gameplay.grid_checks import x_wins, impossible, o_wins, draw
from gameplay.player_moves import process_players_move
from generic.generic import convert_string_to_list


def run_game():
    modified_grid = convert_string_to_list('         ')
    print_grid(modified_grid)
    symbol = 'X'

    while True:
        process_players_move(modified_grid, symbol)
        print_grid(modified_grid)

        if impossible(modified_grid):
            print('Impossible')
            break
        elif x_wins(modified_grid):
            print('X wins')
            break
        elif o_wins(modified_grid):
            print('O wins')
            break
        elif draw(modified_grid):
            print('Draw')
            break
        symbol = 'O' if symbol == 'X' else 'X'
