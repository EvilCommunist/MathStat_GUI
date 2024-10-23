from handlers_functions.standard_functions.standart_functions import lg, log2, sqrt


def get_sort_data(data: list[int] | list[float]) -> list[int] | list[float]:
    return sorted(data)


def get_intervals(data: list[int] | list[float]) -> list:
    n = int(5 * lg(len(data)))
    int_begin = data[0]
    h = (data[-1] - int_begin)/n
    interval_list = [(int_begin + h*i) for i in range(0, n)]
    return interval_list


def get_intervals1(data: list[int] | list[float]) -> list:  # Сделать возможность выбора функции рассчёта
    n = int(sqrt(len(data)))
    int_begin = data[0]
    h = (data[-1] - int_begin) / n
    interval_list = [(int_begin + h * i) for i in range(0, n)]
    return interval_list


def get_intervals2(data: list[int] | list[float]) -> list:
    n = int(log2(len(data)+1))
    int_begin = data[0]
    h = (data[-1] - int_begin) / n
    interval_list = [(int_begin + h * i) for i in range(0, n)]
    return interval_list


def get_quartile(sorted_data: list[int] | list[float], num_of_quartile: int = 1) -> float | int | Exception:
    try:
        if num_of_quartile < 0 or num_of_quartile > 4:
            raise Exception("Некорректное значение квартиля")
    except Exception as ex:
        return ex
    return sorted_data[int(len(sorted_data) * 0.25 * num_of_quartile)]
