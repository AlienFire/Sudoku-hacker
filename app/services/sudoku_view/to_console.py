from app.services.sudoku_view.base import SudokuViewInterface

class SudokuConsoleView(SudokuViewInterface):
    """ Класс для вывода решения в консоль"""
    
    def show (self, solution: list[list]) -> None: 
        """Метод для вывода решения в консоль"""
        print("- - - - - - - - -")
        for row in solution:
            str_row = map(str,row)
            out = ','.join(str_row)
            print(out)
        print("- - - - - - - - -")

