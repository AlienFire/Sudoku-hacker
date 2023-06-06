from copy import deepcopy
from sudoku import Sudoku
from tools import sorted_dict, get_sudoku_task, view_sudoku

# FILE_NAME = "moc_hard_sudoku.json"
# FILE_NAME = "moc_sudoku.json"
FILE_NAME = "moc_hard_sudoku.json"


sudoku = Sudoku(
    board=get_sudoku_task(file_name=FILE_NAME),
)


def solution_attempt(sudoku: Sudoku):
    empty_cells = sudoku.get_empty_cells()

    flag_exit = True
    while flag_exit and empty_cells:
        flag_exit = False
        new_empty_cells = {}

        for cell_idx in empty_cells:
            row_number, column_number = cell_idx

            empty_cells[cell_idx] = empty_cells[cell_idx] - \
                sudoku.get_row(row_number=row_number)

            empty_cells[cell_idx] = empty_cells[cell_idx] - \
                sudoku.get_column(column_number=column_number)

            empty_cells[cell_idx] = empty_cells[cell_idx] - sudoku.get_square(
                row_number=row_number, column_number=column_number)

            if len(empty_cells[cell_idx]) == 0:
                raise Exception("Wrong cell")

            if len(empty_cells[cell_idx]) == 1:
                sudoku.set_cell_value(
                    row_number=row_number,
                    column_number=column_number,
                    possible_value=list(empty_cells[cell_idx])[0],
                )
                flag_exit = True
            else:
                new_empty_cells[cell_idx] = empty_cells[cell_idx]

        empty_cells = new_empty_cells

    return sudoku, sorted_dict(empty_cells)


def deep_solution(sudoku: Sudoku):
    sudoku, empty_cells = solution_attempt(sudoku=sudoku)
    if sudoku.is_solved():
        return sudoku.board

    for cell_idx in empty_cells:
        cell_vals = empty_cells[cell_idx]
        for val in cell_vals:
            new_sudoku = deepcopy(sudoku)
            new_sudoku.set_cell_value(
                row_number=cell_idx[0],
                column_number=cell_idx[-1],
                possible_value=val,
            )
            try:
                return deep_solution(new_sudoku)
            except Exception:
                continue

    return sudoku.board


view_sudoku(deep_solution(sudoku=sudoku))
