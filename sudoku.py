import json
from tools import get_without_stars
FULL_COLLECTION = {1, 2, 3, 4, 5, 6, 7, 8, 9}
SQ_SIZE = 3


class Sudoku:
    board: list[list]

    def __init__(self, board: list[list]) -> None:
        self.board = board

    def get_row(self, row_number: int) -> list:
        """Получение всей строки по индексу"""
        if row_number < 9:
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
        for i in range(sq_row*3, sq_row*3+3):
            for j in range(sq_column*3, sq_column*3+3):
                square_colection.append(self.board[i][j])
        return get_without_stars(square_colection)

    def is_solved(self) -> bool:
        """Проверяет есть ли пустые значения в судоку"""
        for row in self.board:
            if "*" in row:
                return False

        return True

    def get_empty_cells(self) -> dict:
        """Возвращает список всех коордитат в кортежах"""
        empty_cells = {}
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] == "*":
                    empty_cells[(x, y)] = FULL_COLLECTION
        return empty_cells

    def set_cell_value(self, row_number, column_number, possible_value):
        """Устанавливает значение в ячейку"""
        self.board[row_number][column_number] = possible_value
        return self.board


def get_sudoku_task(file_name) -> list[list]:
    with open(file_name) as f:
        data = json.load(f)
    return data.get('board')
