from settings import EMPTY_VAL


def get_without_stars(line: list) -> set:
    """Возвращает список значений без * """
    return {val for val in line if val != EMPTY_VAL}


def sorted_dict(raw_dict: dict[tuple, set], reverse: bool = False) -> dict[tuple, set]:
    """Ф-ия для сортивроки словарая по длине значения"""
    return dict(
        sorted(
            raw_dict.items(),
            key=lambda item: len(item[1]),
            reverse=reverse,
        )
    )


def check_empty_cell(cell_values: list) -> None:
    """Ф-ия проверки отсутствия возможных значений"""
    if len(cell_values) == 0:
        raise Exception("Wrong cell")
