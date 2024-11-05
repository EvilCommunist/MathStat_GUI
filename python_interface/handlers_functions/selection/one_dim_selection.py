from handlers_functions.standard_functions.standart_functions import lg, log2, sqrt
from handlers_functions.standard_functions.r_functions import quartiles


def get_sort_data(data: list[int] | list[float]) -> list[int] | list[float]:
    return sorted(data)


def get_intervals_brkr(data: list[int] | list[float]) -> list:
    n = int(5 * lg(len(data)))
    int_begin = data[0]
    h = (data[-1] - int_begin)/n
    interval_list = [(int_begin + h*i) for i in range(0, n)]
    return interval_list


def get_intervals_hhgd(data: list[int] | list[float]) -> list:
    n = int(sqrt(len(data)))
    int_begin = data[0]
    h = (data[-1] - int_begin) / n
    interval_list = [(int_begin + h * i) for i in range(0, n)]
    return interval_list


def get_intervals_sturgess(data: list[int] | list[float]) -> list:
    n = int(log2(len(data)+1))
    int_begin = data[0]
    h = (data[-1] - int_begin) / n
    interval_list = [(int_begin + h * i) for i in range(0, n)]
    return interval_list


def get_intervals(formula: str, data: list[int] | list[float]):
    if formula == "Брукс-Каррузер":
        return get_intervals_brkr(data)
    elif formula == "Хайнхольд-Гёде":
        return get_intervals_hhgd(data)
    else:
        return get_intervals_sturgess(data)


def get_quartile(sorted_data: list[int] | list[float], num_of_quartile: int = 0) -> float | int | Exception:
    try:
        if num_of_quartile < 0 or num_of_quartile >= 4:
            raise Exception("Некорректное значение квартиля")
    except Exception as ex:
        return ex
    return quartiles(sorted_data)[num_of_quartile]
