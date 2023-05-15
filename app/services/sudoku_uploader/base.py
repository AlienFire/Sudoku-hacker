from abc import ABC, abstractmethod

class SudokuUploaderInterface(ABC):
    """Интерфейс загрузчика судоку"""
    @abstractmethod
    def get_sudoku_task(self) -> list[list]:
       raise NotImplementedError()
