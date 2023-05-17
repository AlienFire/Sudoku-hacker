from abc import ABC, abstractmethod

class SudokuViewInterface(ABC):
    """Интерфейс вывода решённого судоку"""
    @abstractmethod
    def show (self, solution: list[list]) -> None:
       raise NotImplementedError()
