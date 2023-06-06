
import json


empty_cells = {}

FULL_COLLECTION = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def get_options_of_values(row: list, column: list, square: list):
    """Возвращает все возможные значения ячейки без проверки с предыдущими сохраниниями"""
    possible_values = FULL_COLLECTION - \
        set(row) - set(column) - set(square)
    return possible_values


def get_full_values(
    row: list,
    column: list,
    square: list,
    row_number: int,
    column_number: int,
):
    """Возвращает возможные значения используя предыдущий опыт"""
    if (row_number, column_number) not in empty_cells:
        possible_values = get_options_of_values(
            row=row,
            column=column,
            square=square,
        )
        empty_cells[(row_number, column_number)] = possible_values
        return possible_values
    else:
        possible_values = empty_cells.get(
            (row_number, column_number)) - set(row) - set(column) - set(square)
        empty_cells[(row_number, column_number)] = possible_values
        return possible_values


def get_without_stars(line: list) -> set:
    """Возвращает список значений без * """
    return {val for val in line if val != "*"}


def sorted_dict(raw_dict: dict[tuple, set], reverse: bool = False) -> dict[tuple, set]:
    """Ф-ия для сортивроки словарая по длине значения"""
    return dict(
        sorted(
            raw_dict.items(),
            key=lambda item: len(item[1]),
            reverse=reverse,
        )
    )


def get_sudoku_task(file_name) -> list[list]:
    with open(file_name) as f:
        data = json.load(f)
    return data.get('board')


def view_sudoku(board: list[list]) -> None:
    """Ф-ия для удобного вывода судоку"""
    if not board:
        return
    for row in board:
        print(" ".join(map(str, row)))
