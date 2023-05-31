def non_numeric_value_validation(coordinates):
    updated_coordinates = []
    try:
        for value in coordinates:
            int_value = int(value)
            updated_coordinates.append(int_value - 1)
        return updated_coordinates
    except TypeError:
        print('You should enter numbers!')
        return True


def is_place_free_validation(grid, coordinates):
    if ' ' not in grid[coordinates[0]][coordinates[1]]:
        print('This cell is occupied! Choose another one!')
    else:
        return True


def coordinates_range_validation(coordinates):
    coor_range = ['1', '2', '3']
    if (coordinates[0] not in coor_range
            or coordinates[1] not in coor_range):
        print('Coordinates should be from 1 to 3!')
        return True
