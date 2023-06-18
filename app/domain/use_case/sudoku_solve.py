from copy import deepcopy

from app.domain.entity.sudoku import Sudoku
from app.services.sudoku_uploader.base import SudokuUploaderInterface
from app.services.sudoku_view.base import SudokuViewInterface
from tools import check_empty_cell, sorted_dict


class Solver():
    _uploader: SudokuUploaderInterface
    _viewer: SudokuViewInterface

    def __init__(
        self,
        uploader: SudokuUploaderInterface,
        viewer: SudokuViewInterface,
    ) -> None:
        self._uploader = uploader
        self._viewer = viewer

    def execute(self):
        sudoku = Sudoku(
            board=self._uploader.get_sudoku_task(),
        )
        solved_sudoku = Solver.deep_solution(sudoku=sudoku)
        self._viewer.show(solution=solved_sudoku)

    @staticmethod
    def deep_solution(sudoku: Sudoku):
        sudoku, empty_cells = Solver.solution_attempt(sudoku=sudoku)
        if sudoku.is_solved():
            return sudoku.board

        for cell_idx in empty_cells:
            cell_vals = empty_cells[cell_idx]
            for val in cell_vals:
                new_sudoku = deepcopy(sudoku)
                new_sudoku.set_cell_value(
                    cell_idx=cell_idx,
                    possible_value=val,
                )
                try:
                    return Solver.deep_solution(new_sudoku)
                except Exception:
                    continue

        return sudoku.board

    @staticmethod
    def solution_attempt(sudoku: Sudoku):
        empty_cells = sudoku.get_empty_cells()

        flag_exit = True
        while flag_exit and empty_cells:
            flag_exit = False
            new_empty_cells = {}

            for cell_idx in empty_cells:
                row_number, column_number = cell_idx

                row_values = sudoku.get_row(row_number=row_number)
                coulumn_values = sudoku.get_column(column_number=column_number)
                square_values = sudoku.get_square(
                    row_number=row_number,
                    column_number=column_number,
                )

                empty_cells[cell_idx] = empty_cells[cell_idx] - row_values
                empty_cells[cell_idx] = empty_cells[cell_idx] - coulumn_values
                empty_cells[cell_idx] = empty_cells[cell_idx] - square_values

                check_empty_cell(empty_cells[cell_idx])

                if len(empty_cells[cell_idx]) == 1:
                    sudoku.set_cell_value(
                        cell_idx=cell_idx,
                        possible_value=list(empty_cells[cell_idx])[0],
                    )
                    flag_exit = True
                else:
                    new_empty_cells[cell_idx] = empty_cells[cell_idx]

            empty_cells = new_empty_cells

        return sudoku, sorted_dict(empty_cells)
