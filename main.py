from app.services.sudoku_uploader.from_json import SudokuJsonUploaderService
from app.services.sudoku_view.to_console import SudokuConsoleView
from app.domain.use_case.sudoku_solve import Solver

FILE_NAME = "moc_hard_sudoku.json"

sudoku_solver = Solver(
    uploader=SudokuJsonUploaderService(file_name=FILE_NAME),
    viewer=SudokuConsoleView(),
)

sudoku_solver.execute()
