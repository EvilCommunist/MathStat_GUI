from handlers_functions.standard_functions.standart_functions import lg, log2, sqrt


def get_sort_data(data: list[int] | list[float]) -> list[int] | list[float]:
    return sorted(data)


def get_intervals(data: list[int] | list[float]) -> int:
    return int(5*lg(len(data)))


def get_intervals1(data: list[int] | list[float]) -> int:  # Сделать возможность выбора функции рассчёта
    return int(sqrt(len(data)))


def get_intervals2(data: list[int] | list[float]) -> int:
    return int(log2(len(data)+1))


def get_quartile(sorted_data: list[int] | list[float], num_of_quartile: int = 1) -> float | int | Exception:
    try:
        if num_of_quartile < 0 or num_of_quartile > 4:
            raise Exception("Некорректное значение квартиля")
    except Exception as ex:
        return ex
    return sorted_data[int(len(sorted_data) * 0.25 * num_of_quartile)]
