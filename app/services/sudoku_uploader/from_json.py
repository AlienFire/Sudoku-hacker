import json

from .base import SudokuUploaderInterface

class SudokuJsonUploaderService(SudokuUploaderInterface):
    file_name:str
    
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def get_sudoku_task(self) -> list[list]:
        with open(self.file_name) as f:
            data = json.load(f)
        return data.get('board')