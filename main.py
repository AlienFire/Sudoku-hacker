from app.services.sudoku_uploader import SudokuJsonUploaderService, SudokuUploaderInterface
from app.services.sudoku_view import SudokuConsoleView, SudokuViewInterface


class SudokuSolution():
    _task_uploader: SudokuUploaderInterface
    _solution_view: SudokuViewInterface

    def __init__(
        self,
        task_uploader: SudokuUploaderInterface,
        solution_view: SudokuViewInterface,
    ) -> None:
        self._task_uploader = task_uploader
        self._solution_view = solution_view

    def execute(self) -> None:
        sudoku_task = self._task_uploader.get_sudoku_task()
        self._solution_view.show(sudoku_task)


json_uploader = SudokuJsonUploaderService(file_name="moc_sudoku.json")
sudoku_view = SudokuConsoleView()

ss = SudokuSolution(
    task_uploader=json_uploader,
    solution_view=sudoku_view
)

ss.execute()