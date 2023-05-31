from gameplay.validations import (non_numeric_value_validation, is_place_free_validation,
                         coordinates_range_validation)
from generic.generic import update_the_grid


def process_players_move(grid, symbol):
    while True:
        players_move = input()
        coordinates_lst = players_move.split()
        upd_coordinates = non_numeric_value_validation(coordinates_lst)
        if upd_coordinates is True:
            continue
        if coordinates_range_validation(coordinates_lst):
            continue
        if is_place_free_validation(grid, upd_coordinates):
            break
    update_the_grid(grid, upd_coordinates, symbol)
