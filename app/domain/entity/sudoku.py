from tools import get_without_stars
from settings import EMPTY_VAL
from app.domain.entity.constants import (
    SUDOKU_SIZE,
    FULL_COLLECTION,
    SQ_SIZE,
)


class Sudoku:
    board: list[list]

    def __init__(self, board: list[list]) -> None:
        self.board = board

    def get_row(self, row_number: int) -> list:
        """Получение всей строки по индексу"""
        if row_number < SUDOKU_SIZE:
            return get_without_stars(self.board[row_number])
        return {}

    def get_column(self, column_number: int) -> list:
        """Получение всей колонки по индексу"""
        column = [row[column_number] for row in self.board]
        return get_without_stars(column)

    def get_square(self, row_number, column_number):
        """Получение значений квадрата по индексу колонок """
        sq_row = row_number // SQ_SIZE
        sq_column = column_number // SQ_SIZE
        square_colection = []
        for i in range(sq_row * 3, sq_row * 3 + 3):
            for j in range(sq_column * 3, sq_column * 3 + 3):
                square_colection.append(self.board[i][j])
        return get_without_stars(square_colection)

    def is_solved(self) -> bool:
        """Проверяет есть ли пустые значения в судоку"""
        for row in self.board:
            if EMPTY_VAL in row:
                return False

        return True

    def get_empty_cells(self) -> dict:
        """Возвращает список всех коордитат в кортежах"""
        empty_cells = {}
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] == EMPTY_VAL:
                    empty_cells[(x, y)] = FULL_COLLECTION
        return empty_cells

    def set_cell_value(self, cell_idx: tuple[int], possible_value):
        """Устанавливает значение в ячейку"""
        row_number, column_number = cell_idx
        self.board[row_number][column_number] = possible_value
        return self.board
